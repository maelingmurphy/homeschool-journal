from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

naming_convention = {
   "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s" 
}

db = SQLAlchemy(app=app, metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)

# Adds requirement for users to be logged in, in order to view certain pages
# Redirects user to login page if they visit page that has login requirement and they're not logged in
login.login_view = 'login'

from app import routes, models

# CODE BELOW THAT NEEDS TO BE TESTED




#def create_app():
    # Flask app creation 
    #app = Flask(__name__, instance_relative_config=True) # Refers to this current file 

    # Set app configuration variables 
    #if app.config['ENV'] == 'production':
    #    app.config.from_object('config.ProductionConfig')
    #else:
    #    app.config.from_object('config.DevelopmentConfig')

   

   

    

    #print(f'ENV is now set to: {app.config["ENV"]}')

    #return app


