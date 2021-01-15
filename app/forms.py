from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, BooleanField, SubmitField # Field Types
from wtforms.fields.html5 import DateField # Renders datepicker
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo # Validators
from app.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
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

class AddActivity(FlaskForm):
    """Add activity form."""
    
    # Activity Title 
    title = StringField('Title', validators=[DataRequired()])

    # Activity Description
    description = TextAreaField('Activity Description')

    # Select subject
    subject = SelectField(u'Subject', choices=[])
    resources = TextAreaField('Resources')

    # Select student(s)
    student = SelectField(u'Student(s)', choices=[])

    # Activity date selector
    activity_date = DateField('Activity Date', format='%Y-%m-%d', validators=[DataRequired()])
    
    # Checkbox for marking completed activity
    status = BooleanField('Activity Completed?')

    # Additional Notes
    notes = TextAreaField('Notes')

    # Submit form
    submit = SubmitField('Add Activity')

