from flask_login import login_required, current_user
from flask import Blueprint, render_template
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .models import User
from . import db

geolocator = Nominatim(user_agent='myapp')
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
        global res
        res = {}
        all_cities = []
        # Détermination de la ville du match
        for i in range(len(nb_user)): # Pour chaque utilisateur
            all_cities.append(nb_user[i].localisation) # Ajouter chaque ville
        find_closer(all_cities, current_user.localisation) # Trouver la ville la plus proche
        # Détermination du sexe du match
        if (current_user.orientation == "Homosexuel"):
            match_sexe = current_user.sexe
        elif (current_user.sexe == 'Femme'):
            match_sexe = 'Homme'
        else:
            match_sexe = 'Femme'
        # Détermination de l'âge du match
        for i in range(current_user.age - 5, current_user.age + 5): # Dans un rayon de 10 ans d'écart
            Matchs = User.query.filter_by(localisation = listToString(res), sexe = match_sexe, orientation = current_user.orientation, age = i).all() # Essayer de trouver un utilisateur avec les critères suivants
            if Matchs: # Si un utilisateur est trouvé
                break # Stopper la boucle
        return render_template('match.html', len=len(Matchs), Matchs=Matchs)


def find_closer(all_cities, city): # Cette fonction retrouve la ville la plus proche d'une ville donnée en paramètre à partir d'une liste de plusieurs villes
    all_cities.remove(city) # Enlever la ville considérée comme point de départ
    city = geolocator.geocode(city) # Obtenir les coordonnées de la ville départ
    global res
    cities = {}
    for i in range(0, len(all_cities)): # Pour chaque ville dans la liste
        cities[all_cities[i]] = geolocator.geocode(all_cities[i]) # Ajout dans le dictionnaire du détail de chaque ville
        res[all_cities[i]] = cities[all_cities[i]].latitude, cities[all_cities[i]].longitude # Ajout dans le dictionnaire du nom chaque ville et de ses coordonnées
    for i in range(0, len(all_cities)): # Pour chaque ville dans la liste
        res[all_cities[i]] = round(geodesic((res[all_cities[i]]), (city.latitude, city.longitude)).km) # Calcul de la distance entre le point de départ et chaque ville 
    tmp = min(res.values()) # Déterminer distance la plus basse à partir des valeurs 
    res = [key for key in res if res[key] == tmp] # Retrouver le nom de la ville correspondante
    return res

def listToString(list):
    base = ''
    return base.join(list)