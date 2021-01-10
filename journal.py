from app import app

from flask import (
    Flask, 
    render_template, 
    url_for,
    redirect
)

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Flask app creation 
app = Flask(__name__, instance_relative_config=True) # Refers to this current file 

#app.config.from_pyfile('config.py') # Load configuration variables from an instance folder

# Set app configuration variables 
if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

print(f'ENV is now set to: {app.config["ENV"]}')

if __name__ == "__app__":
    app.run(debug=True)

# Database instance
db = SQLAlchemy(app) # db object that represents the database 

# Database migration instance
migrate = Migrate(app, db) # migrate object that represents the migration engine 

# Import AddActivity class from forms.py
from forms import AddActivity 

