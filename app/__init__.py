from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)

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


