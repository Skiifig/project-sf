from flask_login import login_required, current_user
from flask import Blueprint, render_template
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
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
    if len(nb_user) < 10: # S'il y a moins de 10 inscrits
        return "ERREUR : La base doit comporter au moins 10 utilisateurs pour pouvoir faire un match", 502 # Redirection vers une page d'erreur
    else:
        all_cities = []
        first_request = User.query.filter(User.localisation==current_user.localisation).all()
        for i in range(len(nb_user)):
            all_cities.append(nb_user[i].localisation)
        Matchs = User.query.filter(User.sexe=='Femme').limit(3).all()
        return render_template('match.html', len=len(Matchs), Matchs=Matchs, request=request)