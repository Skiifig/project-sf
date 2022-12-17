from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(20))