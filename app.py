from flask import (
    Flask, 
    render_template, 
    url_for,
    redirect
)

from config import Config

# Import AddActivity class from forms.py
from forms import AddActivity 


# Flask app creation 
app = Flask(__name__, instance_relative_config=True) # Refers to this current file 

#app.config.from_pyfile('config.py') # Load configuration variables from an instance folder

if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

print(f'ENV is now set to: {app.config["ENV"]}')

if __name__ == "__app__":
    app.run(debug=True)

# Home Page
@app.route('/')
def index():
    return render_template('index.html')


# Add Activity 
@app.route('/add', methods=('GET', 'POST'))
def add():
    form = AddActivity()
    if form.validate_on_submit():
        return 'Activity has been added'

    return render_template(
        'add.html',
        form=form
    )

# Activity Log
@app.route('/log')
def log():
    form = AddActivity()
    if form.validate_on_submit():
        return 'Activity has been added'

    return render_template(
        'log.html',
        form=form
    )