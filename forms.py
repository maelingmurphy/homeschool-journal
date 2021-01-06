from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SelectField, SubmitField # Field Types
from wtforms.validators import DataRequired, Length # Validators

class AddActivity(FlaskForm):
    """Add activity form."""
    title = StringField(
        'Title',
        [DataRequired()]
    )
    description = TextField(
        'Activity Description',
    )
    subject = SelectField(u'Subject', choices=[('math', 'Math'), ('read', 'Reading'), ('sci', 'Science')])
    submit = SubmitField('Add Activity')