from app import app


from flask import (
    render_template, 
    url_for,
    redirect
)


# Import AddActivity class from forms.py
#from forms import AddActivity 



# THE ROUTES 

# Home Page
@app.route('/')
def index():
    date = 'Sunday - January 10, 2020'
    return render_template('index.html', date=date )


# Add Activity 
#@app.route('/add', methods=('GET', 'POST'))
#def add():
#    form = AddActivity()
#    if form.validate_on_submit():
#        return 'Activity has been added'

#    return render_template(
#        'add.html',
#        form=form
#    )

# Activity Log
@app.route('/log')
def log():
    activities = [
        {'date': 'January 10, 2020',
        'title': 'Intro to Multiplication',
        'subject': 'Math',
        'student': 'James',
        'status': 'completed'},
        {'date': 'January 10, 2020',
        'title': 'Prisms',
        'subject': 'Physics',
        'student': 'James',
        'status': 'completed'}
    ]

    return render_template('log.html', activities=activities)

#    form = AddActivity()
#    if form.validate_on_submit():
#        return 'Activity has been added'

#    return render_template(
#        'log.html',
#        form=form
#    )