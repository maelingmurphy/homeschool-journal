from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SelectField, BooleanField, SubmitField # Field Types
from wtforms.fields.html5 import DateField # Renders datepicker
from wtforms.validators import DataRequired # Validators

class AddActivity(FlaskForm):
    """Add activity form."""
    
    # Activity Title 
    title = TextField('Title', validators=[DataRequired()])

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