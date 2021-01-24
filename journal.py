from app import app, db
from app.models import User, Student, Subject, Attendance

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Student': Student, 'Subject': Subject, 'Attendance': Attendance}