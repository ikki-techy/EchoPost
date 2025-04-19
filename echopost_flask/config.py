import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'f1b3cf34b2e5a8d2c54ad'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


