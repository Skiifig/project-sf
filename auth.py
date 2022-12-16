from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get("email") # Obtenir valeur de l'email entré
    password = request.form.get("password") # Obtenir valeur du mot de passe entré
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first() # Obtenir la ligne de l'utilisateur dans la base de données

    if not user or not check_password_hash(user.password, password): # Si l'email ou le mot de passe sont faux
        flash('Votre adresse mail ou votre mot de passe est incorrect') # Renvoyer l'erreur dans la page
        return redirect(url_for('auth.login')) # Redirection vers la page de connexion
    login_user(user, remember=remember) # Sinon connecter utilisateur
    return redirect(url_for('main.profile')) # Afficher la page de profil

@auth.route('/signup')
def signup():
    return render_template("registration.html")

@auth.route('/signup', methods=['POST'])
def signup_post():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")
    user = User.query.filter_by(email=email).first()
    if user:
        return redirect(url_for(auth.signup))
    new_user = User(fname=fname, lname=lname, email=email, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user) # Ajouter l'utilisateur à la base de données
    db.session.commit() # Mettre la base de données à jour
    return redirect(url_for("auth.login"))

@auth.route('/deconnexion')
@login_required
def logout():
    logout_user() # Déconnexion de l'utilisateur
    return redirect(url_for('main.index')) # Redirection vers la page index