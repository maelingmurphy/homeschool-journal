import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f"postgresql://{os.environ.get('db_username')}:{os.environ.get('db_password')}@localhost:5432/{os.environ.get('db_name')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')