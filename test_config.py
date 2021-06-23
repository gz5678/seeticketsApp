import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = "sqlite:///test_app.db"
SECRET_KEY = 'dev_test'
TESTING = True
