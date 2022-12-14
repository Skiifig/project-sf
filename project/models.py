from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # Clé primaire
    profile_pic = db.Column(db.String(100))
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(20))
    age = db.Column(db.Integer)
    sexe = db.Column(db.String(10))
    localisation = db.Column(db.String(20))
    orientation = db.Column(db.String(10))
    hobbies = db.Column(db.String(100))