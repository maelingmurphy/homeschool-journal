from flask import (
    render_template, 
    url_for,
    redirect,
    flash,
    request
)

from app import app, db
from app.forms import LoginForm, AddSubjectForm, AddStudentSubjectForm, AddActivityForm, RegistrationForm # Import classes from forms.py
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Student, Activity
from werkzeug.urls import url_parse



# THE ROUTES 

# Home Page
@app.route('/',  methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required 
def index():
    date = 'Sunday - January 17, 2020'
    
    # Add Student and Subject Form Info
    form = AddSubjectForm()
    if form.validate_on_submit():
        
        # Get student number
        student_number = int(form.user_student.data)

        # Get student names
        student_names = []
        for i in range(1, student_number + 1):
            student_names.append(request.form.get(f"student_name{i}"))

        # Add student names with current user id to database
        for name in student_names:
            student = Student(student_name=name, user_id=current_user.id)
            db.session.add(student)
            db.session.commit() 
        
        # Add student_number to user table 
        current_user.student_number = student_number
        db.session.commit()

        # Flash Message Confirmation
        for name in student_names:
            flash('You have successfully added {} as a student!'.format(name), 'info')


        # Get subject number
        #subject_number = int(form.user_subject.data)

        # Get subject names
        #subject_names = []
        #for i in range(1, subject_number + 1):
            #subject_names.append(request.form.get(f"subject_name{i}"))

        # Add subject names with current user id to database
        #for name in subject_names:
            #subject = Subject(subject_name=name, admin=current_user.id)  
            #db.session.add(subject) 
            #db.session.commit()

            
        
        # Flash message confirmation
        #flash('You have successfully added the subject(s): {} '.format(subject_names), 'info')


        return redirect(url_for('index'))
       
        
        
        # Test
        #print("User id: ", current_user.id)
        #print("Number of students: ", student_number)
        #print("Student Names", student_names) 

        

    return render_template('index.html', date=date, form=form)

# Register User
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)   
        db.session.add(user)
        db.session.commit()  
        username = form.username.data
        flash('Congratulations {}, you are now a registered user!'.format(username), 'info')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# Add Activity 
@app.route('/add', methods=('GET', 'POST'))
@login_required
def add():
    
    # Create mock subject and student objects to populate SelectField choices in forms.py until database is created
    students = ['James', 'Stephanie', 'Mariah']
    subjects = ['Math', 'Reading', 'Science', 'Geography', 'Physical Education', 'Music', 'Foreign Language']

    form = AddActivityForm()
    form.subject.choices = subjects
    form.student.choices = students

    if form.validate_on_submit():
        # Add activity info to database 
        
        # Display flash confirmation message
        flash('"{}" has been successfully added'.format(form.title.data), 'info')
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

    form = AddActivityForm()
    if form.validate_on_submit():
        # Display flash confirmation message
        flash('"{}" has been successfully added'.format(form.title.data), 'info')

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
            flash('Invalid username or password', 'error')
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
