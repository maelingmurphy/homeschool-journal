from flask import (
    Flask, 
    render_template, 
    url_for,
    redirect
)
from app import app

# Import AddActivity class from forms.py
from forms import AddActivity 



# THE ROUTES 

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