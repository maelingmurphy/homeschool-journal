import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Config class and set default attributes 
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'testingRANDOMkey801e982734019G825g7!084560A2398571R%03874023;46E984701298437'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # signals the application every time a change is about to be made in the database

# Config class for running in production
class ProductionConfig(Config):
    pass

# Config class for running in development
class DevelopmentConfig(Config):
    DEBUG = True

# Config class for testing
class TestingConfig(Config):
    TESTING = True 