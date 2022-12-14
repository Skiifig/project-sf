from flask import Blueprint, render_template
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/connexion')
def login():
    return render_template("login.html")

@auth.route('/inscription')
def signup():
    return render_template("registration.html")

@auth.route('/deconnexion')
def logout():
    return 'Logout'