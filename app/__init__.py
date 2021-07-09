from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_login import LoginManager
import datetime
from datetime import datetime


app = Flask(__name__)
app.config.from_object(Config)

naming_convention = {
   "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s" 
}

# Create custom filters to use on Jinja template variables
@app.template_filter()
def datetime_format_filter(value, format='%B %d, %Y'):
    """Convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetime_format_filter'] = datetime_format_filter

@app.template_filter()
def datetime_day_format_filter(value, format='%A - %B %d, %Y'):
    """Convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetime_day_format_filter'] = datetime_day_format_filter

@app.template_filter()
def datepicker_format_filter(value, format='%Y-%m-%d'):
    """Convert date to format compatible with datepicker."""
    return value.strftime(format)

app.jinja_env.filters['datepicker_format_filter'] = datepicker_format_filter


@app.template_filter()
def string_to_datetime_filter(value):
    """Convert string to datetime object."""
    return datetime.strptime(value, '%Y-%m-%d')

app.jinja_env.filters['string_to_datetime'] = string_to_datetime_filter


# Create database instance 

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


