from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SelectMultipleField, BooleanField, SubmitField # Field Types
from wtforms.fields.html5 import DateField # Renders datepicker
from wtforms.validators import ValidationError, DataRequired, InputRequired, Email, EqualTo # Validators
from app.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Please enter a username")])
    email = StringField('Email', validators=[DataRequired(), Email("Please enter your email address")])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match")])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email address is already registered.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class AddStudentSubjectForm(FlaskForm):
    """Add student(s) and subject(s) form."""
    user_student = SelectField('How many students do you have?', choices=[ 1, 2, 3, 4, 5, 6, 7, 8], validators=[InputRequired()])
    student_name1 = StringField('Student Name(s)', validators=[InputRequired("Please enter student's name")])
    user_subject = SelectField('How many subjects do you teach?', choices=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], validators=[InputRequired()] )
    subject_name1 = StringField('Subject', validators=[InputRequired("Please enter subject name")])
    submit = SubmitField('Update')

class AddStudentForm(FlaskForm):
    student_name = StringField('Student Name(s)', validators=[DataRequired("Please enter student's name")])
    submit = SubmitField('Add')

class AddSubjectForm(FlaskForm):
    subject_name = StringField('Subject', validators=[DataRequired("Please enter subject name")])
    submit = SubmitField('Add')

class AddActivityForm(FlaskForm):
    """Add activity form."""
    
    # Activity Title 
    title = StringField('Title', validators=[DataRequired("Activity title required")])

    # Activity Description
    description = TextAreaField('Activity Description')

    # Select subject
    subject = SelectField(u'Subject', choices=[])
    
    # List resources
    resources = TextAreaField('Resources')

    # Select student(s)
    student = SelectField(u'Student', choices=[])

    # Activity date selector
    activity_date = DateField('Activity Date', format='%Y-%m-%d', validators=[DataRequired()])
    
    # Checkbox for marking completed activity
    status = BooleanField('Activity Completed?')

    # Additional Notes
    notes = TextAreaField('Notes')

    # Submit form
    submit = SubmitField('Add Activity')

class AddAttendanceForm(FlaskForm):
    """Add attendance form"""
    attendance_date = DateField('Select Date', format='%Y-%m-%d')
    student = SelectField(u'Select Student', choices=[])
    submit = SubmitField('Save Entry')

class DisplayActivitiesForm(FlaskForm):
    """Display activites form"""
    display = SelectField(u'Display activities for:', choices=['Today','This Week','Next Week', 'Previous Week'])
    student = SelectField(u'Student', choices=[])
    display_submit = SubmitField('Display Activities')