# Create the Config class and set default attributes 
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'testingRANDOMkey801e982734019G825g7!084560A2398571R%03874023;46E984701298437'

# Config class for running in production
class ProductionConfig(Config):
    pass

# Config class for running in development
class DevelopmentConfig(Config):
    DEBUG = True

# Config class for testing
class TestingConfig(Config):
    TESTING = True 