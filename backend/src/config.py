import os

basedir = os.path.abspath(os.path.dirname(__file__))

#uploaded_data

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = '/usr/src/app/uploadeddata'