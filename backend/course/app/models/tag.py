from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import reconstructor

from app.models.base import Base


class Tag(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)

    @staticmethod
    def get_or_create_tag(tag_name):
        tag_set = Tag.query.filter_by(name=tag_name)
        if tag_set.count() == 0:
            tag = Tag(name=tag_name)
        else:
            tag = tag_set.first()
        return tag

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'name']
