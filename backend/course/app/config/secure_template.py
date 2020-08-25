"""
This is the template for secure.py, please created your own secure.py this way.
"""
import os
from os.path import join

SQLALCHEMY_DATABASE_URI = \
    'mysql+pymysql://root:123456@localhost/name'

# SECRET_KEY = 'Lin Huancheng wudi'
UPLOAD_FOLDER = join(os.path.abspath(os.path.join(os.getcwd())), "static/uploads")
ALLOWED_EXTENSIONS = ['*']
MAX_CONTENT_LENGTH = 1000 * 1024 * 1024  # 1000mb

JWT_SECRET_KEY = 'Lin Huancheng zuishuai'

LOCK_TIMEOUT = 20

# Uncomment this line when testing with pytest
# DEBUG = False
