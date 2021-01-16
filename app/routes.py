from flask import (
    render_template, 
    url_for,
    redirect,
    flash,
    request
)

from app import app, db
from app.forms import LoginForm, AddActivity, RegistrationForm # Import LoginForm, AddActivity classes from forms.py
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse



# THE ROUTES 

# Home Page
@app.route('/')
@app.route('/index')
@login_required 
def index():
    date = 'Sunday - January 10, 2020'
    return render_template('index.html', date=date )

# Register User
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        # Get student number
        student_number = int(form.user_student.data)

        # Get student names
        student_names = []
        for i in range(1, student_number + 1):
            student_names.append(request.form.get(f"student_name{i}"))

        # Add student names to database (ADD USER ID!!)
        for name in student_names:
            student = Student(student_name=name, user_id="")

        # Test
        print(student_number)
        print("Student Names", student_names) 
        
        #db.session.add(user)
        #db.session.commit()

        
        username = form.username.data
        flash('Congratulations {}, you are now a registered user!'.format(username))
        #return redirect(url_for('login'))
    return render_template('register.html', form=form)


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
        # Add activity info to database 
        
        # Display flash confirmation message
        flash('"{}" has been successfully added'.format(form.title.data))
        return redirect(url_for('log'))

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
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
