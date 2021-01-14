from flask import (
    render_template, 
    url_for,
    redirect,
    flash
)

from app import app
from app.forms import LoginForm, AddActivity # Import LoginForm, AddActivity classes from forms.py
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


# THE ROUTES 

# Home Page
@app.route('/')
@app.route('/index')
@login_required 
def index():
    date = 'Sunday - January 10, 2020'
    return render_template('index.html', date=date )


# Add Activity 
@app.route('/add', methods=('GET', 'POST'))
@login_required
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
@login_required
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
@login_required
def attend():
    return render_template('attend.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
