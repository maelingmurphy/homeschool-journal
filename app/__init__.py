from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

# CODE BELOW THAT NEEDS TO BE TESTED

#from config import Config
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

#def create_app():
    # Flask app creation 
    #app = Flask(__name__, instance_relative_config=True) # Refers to this current file 

    # Set app configuration variables 
    #if app.config['ENV'] == 'production':
    #    app.config.from_object('config.ProductionConfig')
    #else:
    #    app.config.from_object('config.DevelopmentConfig')

    #from app import models

    # Database instance
    #db = SQLAlchemy(app) # db object that represents the database 

    # Database migration instance
    #migrate = Migrate(app, db) # migrate object that represents the migration engine 

    #print(f'ENV is now set to: {app.config["ENV"]}')

    #return app


#from app import (
#    routes, 
#    models
#)