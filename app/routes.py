from flask import (
    render_template, 
    url_for,
    redirect,
    flash
)

from app import app
from app.forms import AddActivity # Import AddActivity class from forms.py



# THE ROUTES 

# Home Page
@app.route('/')
def index():
    date = 'Sunday - January 10, 2020'
    return render_template('index.html', date=date )


# Add Activity 
@app.route('/add', methods=('GET', 'POST'))
def add():
    
    # Create mock subject and student objects to populate SelectField choices in forms.py until database is created
    students = ['James', 'Stephanie', 'Mariah']
    subjects = ['Math', 'Reading', 'Science', 'Geography', 'Physical Education', 'Music', 'Foreign Language']

    form = AddActivity()
    form.subject.choices = subjects
    form.student.choices = students

    if form.validate_on_submit():
        # Display flash confirmation message
        flash('"{}" has been successfully added'.format(form.title.data))
        return redirect(url_for('index'))

    return render_template('add.html',form=form, students=students)

# Activity Log
@app.route('/log', methods=('GET', 'POST'))
def log():
    activities = [
        {'date': 'January 10, 2020',
        'title': 'Intro to Multiplication',
        'subject': 'Math',
        'student': 'James',
        'status': 'completed'},
        {'date': 'January 20, 2020',
        'title': 'Prisms',
        'subject': 'Physics',
        'student': 'James',
        'status': 'completed'},
        {'date': 'January 22, 2020',
        'title': 'Solar Power',
        'subject': 'Science',
        'student': 'Mariah',
        'status': 'completed'},
        {'date': 'January 24, 2020',
        'title': 'The Periodic Table of Elements',
        'subject': 'Science',
        'student': 'Mariah',
        'status': 'completed'}

    ]

    form = AddActivity()
    if form.validate_on_submit():
        # Display flash confirmation message
        flash('"{}" has been successfully added'.format(form.title.data))

    return render_template('log.html', activities=activities, form=form)


# Attendance History
@app.route('/attendance')
def attend():
    return render_template('attend.html')
