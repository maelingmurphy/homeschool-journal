from flask_wtf import FlaskForm
from wtforms import validators, TextField, TextAreaField, SelectField, BooleanField, SubmitField # Field Types
from wtforms.fields.html5 import DateField # Renders datepicker
from wtforms.validators import DataRequired # Validators

class AddActivity(FlaskForm):
    """Add activity form."""
    
    # Activity Title 
    title = TextField(
        'Title',
        [DataRequired()]
    )

    # Activity Description
    description = TextAreaField(
        'Activity Description'
    )

    # Select subject
    subject = SelectField(u'Subject', choices=[('math', 'Math'), ('read', 'Reading'), ('sci', 'Science')])
    resources = TextAreaField(
        'Resources'
    )

    # Select student(s)
    students = SelectField(u'Student(s)', choices=[('1', 'Student 1'), ('2', 'Student 2'), ('3', 'All Students')])

    # Activity date selector
    activity_date = DateField('Activity Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    
    # Checkbox for marking completed activity
    status = BooleanField('Completed?')

    # Submit form
    submit = SubmitField('Add Activity')