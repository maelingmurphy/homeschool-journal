from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

# User loader function that laods a user given the ID 
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    students = db.relationship('Student', backref='admin', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    title = db.Column(db.String(150), index=True, nullable=False)
    description = db.Column(db.Text, index=True)
    subject = db.Column(db.String(64), index=True, nullable=False)
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
    attendance = db.Column(db.String(64), index=True)
    activities = db.relationship('Activity', backref='student(s)', lazy='dynamic')

    def __repr__(self):
        return '<Student {}>'.format(self.student_name)

