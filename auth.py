from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/connexion')
def login():
    return render_template("login.html")

@auth.route('/connexion', methods=['POST'])
def login_post():
    email = request.form["email"]
    password = request.form["password"]
    remember = True if request.form["remember"] else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password):
        flash('Votre adresse mail ou votre mot de passe est incorrect')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/inscription')
def signup():
    return render_template("registration.html")

@auth.route('/signup', methods=['POST'])
def signup_post():
    fname = request.form["fname"]
    lname = request.form["lname"]
    email = request.form["email"]
    password = request.form["password"]
    user = User.query.filter_by(email=email).first()
    if user:
        return redirect(url_for(auth.signup))
    new_user = User(fname=fname, lname=lname, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("auth.login"))

@auth.route('/deconnexion')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))