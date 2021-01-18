from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

# User loader function that laods a user given the ID 
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Helper/Association Tables 
student_activity = db.Table('student_activity',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('activity_id', db.Integer, db.ForeignKey('activity.id'))
)

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, index=True, unique=True)
    email = db.Column(db.String(120), nullable=False, index=True, unique=True)
    student_number = db.Column(db.Integer, index=True)
    password_hash = db.Column(db.String(128))
    students = db.relationship('Student', backref='admin', lazy='dynamic')
    subjects = db.relationship('Subject', backref='admin', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), index=True, nullable=False)
    subject_id = db.Column(db.String(64), db.ForeignKey('subject.id'), index=True, nullable=False)
    description = db.Column(db.Text, index=True)
    resources = db.Column(db.Text, index=True)
    activity_date = db.Column(db.String(64), index=True, nullable=False)
    notes = db.Column(db.Text, index=True)
    status = db.Column(db.Integer, index=True, nullable=False)

    def __repr__(self):
        return '<Activity {}>'.format(self.title)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(64), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    attendance = db.relationship('Attendance', backref='student', lazy='dynamic')
    activities = db.relationship('Activity', secondary=student_activity, backref=db.backref('student', lazy='dynamic'))

    def __repr__(self):
        return '<Student {}>'.format(self.student_name)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attendance_date = db.Column(db.String(64), index=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    attendance_status = db.Column(db.Integer, index=True)
    
    def __repr__(self):
        return '<Student {}, Date {}, Attendance {}>'.format(self.student_id, attendance_date, attendance_status)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(64), index=True)
    activities = db.relationship('Activity', backref='subject', lazy='dynamic')

    def __repr__(self):
        return '<Subject>'.format(self.subject_name)

