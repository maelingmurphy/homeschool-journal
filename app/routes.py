from flask import (
    render_template, 
    url_for,
    redirect,
    flash,
    request
)

from app import app, db
from app.forms import LoginForm, AddStudentSubjectForm, AddActivityForm, RegistrationForm # Import classes from forms.py
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Student, Activity, Subject
from werkzeug.urls import url_parse



# THE ROUTES 

# Home Page
@app.route('/',  methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required 
def index():
    date = 'Sunday - January 17, 2020'
    
    # ADD STUDENT & SUBJECT INFO
    form = AddStudentSubjectForm()
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
            flash('You have successfully added {} as a student!'.format(name), 'info')
        
        # Add student_number to user table 
        current_user.student_number = student_number
        db.session.commit()

        # Get subject number
        subject_number = int(form.user_subject.data)

        # Get subject names
        subject_names = []
        for i in range(1, subject_number + 1):
            subject_names.append(request.form.get(f"subject_name{i}"))

        # TEST
        print("Subject Number", subject_number)
        print("Subject Names", subject_names)
        print("Current User ID", current_user.id)

        # Add subject names with current user id to database
        for name in subject_names:
            subject = Subject(subject_name=name)
            subject.admins.append(current_user) # Using backref to associate subject with current user
            db.session.add(subject)
            db.session.commit()

        flash('You have successfully added the subject(s): {} '.format(subject_names), 'info')

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
    
    # Pull user's list of students and objects saved to their User model
    students = current_user.students
    subjects = current_user.subjects

    form = AddActivityForm()

    # Display user's students and subjects as choices 
    form.subject.choices = subjects
    form.student.choices = students

    if form.validate_on_submit():

        # Get subject and student objects
        subject = db.session.query(Subject).filter_by(subject_name=form.subject.data).first()
        student = db.session.query(Student).filter_by(student_name=form.student.data).first()

        # TEST
        print('Subject', subject)
        print('Subject id', subject.id)
        print('Student', student)
        print('Student id', student.id)
        

        # Get activity info variables from form data 
        activity_title = form.title.data
        activity_date = form.activity_date.data
        activity_description = form.description.data
        activity_resources = form.resources.data
        activity_notes = form.notes.data
        activity_status = form.status.data

        # Add activity info to database
        activity = Activity(
            title=activity_title, user_id=current_user.id, student_id=student.id, subject_id=subject.id, 
            description=activity_description, resources=activity_resources,
            activity_date=activity_date, notes=activity_notes, status=activity_status)
        
        db.session.add(activity)
        db.session.commit()

        # Display flash confirmation message
        flash('"{}" has been successfully added'.format(form.title.data), 'info')
        return redirect(url_for('log'))

    return render_template('add.html',form=form, students=students)

# Activity Log
@app.route('/log', methods=('GET', 'POST'))
@login_required
def log():
    activities = current_user.activities

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
