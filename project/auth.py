from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from werkzeug.utils import secure_filename
from .models import User
from . import db
import os

auth = Blueprint('auth', __name__)
global email # Cette variable permet d'avoir accès à l'utilisateur puisque chaque adresse mail est unique

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/login', methods=['POST'])
def login_post():
    global email
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
    global email
    profile_pic = request.files["profilePic"]
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")
    age = request.form.get("age")
    user = User.query.filter_by(email=email).first()
    path_to_picture = '/static/images/' + secure_filename(profile_pic.filename)
    profile_pic.save(os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(profile_pic.filename)))
    if user: # Si l'utilisateur existe déjà
        return redirect(url_for('auth.login')) # Redirection de la page de connexion
    new_user = User(profile_pic=path_to_picture, fname=fname, lname=lname, email=email, password=generate_password_hash(password, method='sha256'), age=age) # Création de l'utilisateur
    db.session.add(new_user) # Ajouter l'utilisateur à la base de données
    db.session.commit() # Mettre la base de données à jour
    return redirect(url_for("auth.confirmation")) # Redirection vers la page de confirmation

@auth.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@auth.route('/confirmation', methods=['POST'])
def confirmation_post():
    global email
    user = User.query.filter_by(email=email).first() # Obtenir l'utilisateur à partir de l'email
    user.sexe = request.form.get("sexe")
    user.localisation = request.form.get("localisation")
    user.orientation = request.form.get("orientation")
    user.hobbies = request.form.get("hobbies")
    db.session.commit()
    return redirect(url_for("auth.login"))

@auth.route('/deconnexion')
@login_required
def logout():
    logout_user() # Déconnexion de l'utilisateur
    return redirect(url_for('auth.login')) # Redirection vers la page index

@auth.route('/delete')
@login_required
def user_delete():
    global email
    user = User.query.filter_by(email=email).first()
    db.session.delete(user) # Suppression de l'utilisateur
    db.session.commit()
    return redirect(url_for('main.index'))