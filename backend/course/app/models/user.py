from urllib.parse import urlencode
from urllib.request import urlopen
from xml.etree import ElementTree
from urllib.parse import quote

from flask import current_app
from sqlalchemy import Column, String, SmallInteger, orm
from sqlalchemy.orm import relationship

from app.libs.enums import UserTypeEnum
from app.libs.error_code import AuthFailed
from app.models.base import Base, db
from app.libs.email import generate_email_auth_token, verify_email_auth_token
from app.libs.email import send_email


class User(Base):
    gid = Column(String(10), primary_key=True)
    email = Column(String(63), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    _auth = Column("auth", SmallInteger)
    favorite_question = relationship('Question', backref='user')
    courses = relationship('Course',
                           secondary='join(Enroll, Course, Enroll.course_cid == Course.cid)',
                           primaryjoin='and_(User.gid == Enroll.user_gid)')
    teaching_courses = relationship('Course',
                                    secondary='join(Enroll, Course, Enroll.course_cid == Course.cid)',
                                    primaryjoin='and_(User.gid == Enroll.user_gid, Enroll.enroll_type >= 2)')
    name = Column(String(24))
    phone = Column(String(24))
    school = Column(String(63))
    photos = relationship('Photo')

    @property
    def belong_author(self):
        return self.gid

    @orm.reconstructor
    def __init__(self):
        super().__init__()
        self.fields = ['gid', 'email', 'nickname', 'auth', 'name', 'phone', 'school']

    @property
    def auth(self):
        return UserTypeEnum(self._auth)

    @auth.setter
    def auth(self, status):
        self._auth = status.value

    @staticmethod
    def verify(ticket, service):
        gid, uid = User.check_ticket(ticket, service)
        # uid can be used to identify the grade of users
        if not gid:
            raise AuthFailed()

        user = User.query.filter_by(gid=gid).first()
        scope = User.assign_scope(user)
        return {
            'gid': gid,
            'scope': scope,
            'uid': uid
        }

    @staticmethod
    def assign_scope(user):
        if not user:
            scope = 'Scope'
        elif user.auth == UserTypeEnum.MANAGER:
            scope = 'AdminScope'
        elif user.auth == UserTypeEnum.TEACHER:
            scope = 'TeacherScope'
        elif user.auth == UserTypeEnum.STUDENT:
            scope = 'StudentScope'
        return scope

    @staticmethod
    def register(nickname, email, gid, uid, redirect_path=None):
        """
        This function is used when user login with ustc-CAS for the first time.
        :param gid: general ID for students and staffs of USTC
        :param uid: student ID(length = 10) or teacher ID(length = 5)
        :return:
        """
        with db.auto_commit():
            user = User()
            user.gid = gid
            user.nickname = nickname
            # email authentication
            email_auth_token = generate_email_auth_token(gid=gid, expiration=600)
            send_email(email, 'Email Authentication', 'email_auth.html', \
                       token=email_auth_token, host=current_app.config['HOST'], nickname=nickname, redirect_path=quote(redirect_path))
            user.email = email
            user.uid = uid
            if len(uid) != 10:
                user.auth = UserTypeEnum.TEACHER
            else:
                user.auth = UserTypeEnum.STUDENT
            db.session.add(user)
            return user

    @staticmethod
    def check_ticket(ticket, service):
        validate = (current_app.config['VALIDATE_URL'] + "?" +
                    urlencode({"service": service, "ticket": ticket}))
        with urlopen(validate) as req:
            tree = ElementTree.fromstring(req.read())[0]
        cas = "{http://www.yale.edu/tp/cas}"
        if tree.tag == cas + "authenticationFailure":
            raise AuthFailed()
        gid = tree.find("attributes").find(cas + "gid").text.strip()
        uid = tree.find(cas + "user").text.strip()
        return gid, uid
