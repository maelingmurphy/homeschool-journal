import logging
from logging.handlers import RotatingFileHandler
import os
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

# Configure the application's logger
if not app.debug and not app.testing:
    if app.config['LOG_TO_STDOUT']:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    else: 
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/homeschool_journal.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Homeschool Journal startup')

from app import routes, models