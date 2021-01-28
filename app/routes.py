from flask import (
    render_template, 
    url_for,
    redirect,
    flash,
    request
)

from app import app, db
from app.forms import LoginForm, AddStudentForm, AddStudentSubjectForm, AddActivityForm, AddAttendanceForm, RegistrationForm # Import classes from forms.py
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Student, Activity, Subject, Attendance
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
            subject = Subject(subject_name=name, user_id=current_user.id)
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
        
        # ADD-ON: Change Boolean to text for status
        if form.status.data:
            activity_status = "Completed"
        else:
            activity_status = "Not Completed"

        # Get activity info variables from form data 
        activity_title = form.title.data
        activity_date = form.activity_date.data
        activity_description = form.description.data
        activity_resources = form.resources.data
        activity_notes = form.notes.data


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
@app.route('/log', methods = ('GET', 'POST'))
@login_required
def log():

    activities = current_user.activities.order_by(Activity.activity_date).all()

    return render_template('log.html', activities=activities)

# Update Activity
@app.route('/update', methods=('GET', 'POST'))
@app.route('/update/<string:title>', methods=('GET', 'POST'))
@login_required
def update(title):

    # Get activity record by title
    activity = db.session.query(Activity).filter_by(title=title).first()
    
    # Pull user's list of students and objects saved to their User model so it can be displayed in form
    students = current_user.students
    subjects = current_user.subjects

    # Set status checkbox 
    if activity.status == "Completed":
        activity_status = True
    else:
        activity_status = False

    # Populate form with user's activity record details
    # (dict key names must match AddActivityForm field names)
    # (dict value names must match Activity model properties in models.py)
    activity_record = {'title': activity.title, 'subject': activity.subject, 'student': activity.student, 'description': activity.description, 'resources': activity.resources, 'notes': activity.notes, 'status': activity_status}
    
    form = AddActivityForm(data=activity_record)

    # Display user's students and subjects as choices for dropdown
    form.subject.choices = subjects
    form.student.choices = students

    # Change submit button label text 
    form.submit.label.text = "Update Activity"

    if form.validate_on_submit():
        
        # Get subject and student objects for accessing student id and subject id
        subject = db.session.query(Subject).filter_by(subject_name=form.subject.data).first()
        student = db.session.query(Student).filter_by(student_name=form.student.data).first()

        # TEST
        print('Subject', subject)
        print('Subject id', subject.id)
        print('Student', student)
        print('Student id', student.id)
        
        # ADD-ON: Change Boolean to text for status
        if form.status.data:
            activity.status = "Completed"
        else:
            activity.status = "Not Completed"

        # Get activity info from form data to update activity record
        activity.title = form.title.data
        activity.activity_date = form.activity_date.data
        activity.description = form.description.data
        activity.resources = form.resources.data
        activity.notes = form.notes.data
        activity.subject_id = subject.id
        activity.student_id = student.id

        # Add activity info to database 
        db.session.commit()

        # Flash confirmation message
        flash('Activity: {} has been updated'.format(activity.title), 'info')

        return redirect(url_for('log'))


    return render_template('update.html', title=title, form=form, activity=activity)

# Activity Details
@app.route('/details/<string:title>')
@login_required
def details(title):
    
    activity = db.session.query(Activity).filter_by(title=title).first()

    return render_template('details.html', title=title, activity=activity)


# Delete Activity
@app.route('/delete/<int:id>')
@login_required
def delete(id):

    # Get activity object by id
    activity = db.session.query(Activity).filter_by(id=id).first()

    # Delete activity from database
    db.session.delete(activity)
    db.session.commit()

    # Flash confirmation message
    flash('Activity record has been removed', 'info')

    return redirect(url_for('log'))



# Attendance History
@app.route('/attendance', methods=('GET', 'POST'))
@login_required
def attend():
    attendance_records = current_user.attendance.order_by(Attendance.attendance_date.desc()).all()

    # Get user's students
    students = current_user.students

    form = AddAttendanceForm()

    # Display user's students and subjects as choices 
    form.student.choices = students
   
    if form.validate_on_submit():
        # Get student id
        student = db.session.query(Student).filter_by(student_name=form.student.data).first()
        # Add attendance data to database
        attendance = Attendance(attendance_date=form.attendance_date.data, student_id=student.id, user_id=current_user.id)
        db.session.add(attendance)
        db.session.commit()
        # Display flash confirmation message
        flash('Attendance on {} has been successfully updated for {}'.format(form.attendance_date.data, form.student.data), 'info')
        return redirect(url_for('attend'))
    return render_template('attend.html', attendance_records=attendance_records, form=form)

# Delete Attendance Record
@app.route('/delete/attendance/<int:id>')
@login_required
def delete_attendance(id):
    # Get attendance object by id
    attendance_record = db.session.query(Attendance).filter_by(id=id).first()

    # Delete attendance record from db
    db.session.delete(attendance_record)
    db.session.commit()

    flash('Attendance record has been removed', 'info')

    return redirect(url_for('attend'))

# Profile
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')

# Edit Profile
@app.route('/profile-edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = AddStudentForm()
    if form.validate_on_submit():
        student = form.student_name.data
        print(student)
        flash('Student {} has been added'.format(student), 'info')
    return render_template('profile-edit.html', form=form)

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
