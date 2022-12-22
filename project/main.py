from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.before_app_first_request
def create_tables():
    db.create_all()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('dashboard.html', name=current_user.fname)

@main.route('/settings')
@login_required
def settings():
    return render_template('settings.html', user=current_user)

@main.route('/match')
@login_required
def match():
    nb_user = User.query.all()
    if len(nb_user) < 10:
        return "ERREUR : La base doit comporter au moins 10 utilisateurs pour pouvoir faire un match", 502
    else:
        return render_template('match.html')