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
    if len(nb_user) < 20: # S'il y a moins de 10 inscrits
        return "ERREUR : La base doit comporter au moins 10 utilisateurs pour pouvoir faire un match", 502 # Redirection vers une page d'erreur
    else:
        Matchs = []
        global dico_city
        dico_city = {}
        global match_sexe
        match_sexe = ''
        global match_city
        get_match_gender(current_user) # Trouver le sexe du match
        get_match_city(nb_user, current_user.localisation) # Trouver la ville la plus proche
        # Détermination de l'âge du match
        while len(Matchs) < 3: # Tant que l'on a pas trouvé 3 matchs potentiels
            for i in range(current_user.age - 10, current_user.age + 10): # Dans un rayon de 10 ans d'écart
                query = User.query.filter_by(sexe = match_sexe, orientation = current_user.orientation, localisation = match_city, age = i).all() # Essayer de trouver un utilisateur avec les critères suivants
                if query != []:
                    Matchs.append(query)
            del dico_city[match_city] # Suppresion de la ville déjà utilisée pour la recherche
            tmp = min(dico_city.values()) # On prend la valeur minimale du dictionnaire
            match_city = [key for key in dico_city if dico_city[key] == tmp] # Retrouver le nom de la ville correspondante
            match_city = match_city[0] # Avant cette ligne match_city est sous forme de tableau
        return render_template('match.html', len=len(Matchs), Matchs=Matchs, request=Matchs)


def get_match_city(nb_user, city): # Cette fonction retrouve la ville la plus proche d'une ville donnée en paramètre à partir d'une liste de plusieurs villes
    global dico_city
    global match_city
    global all_cities
    all_cities = []
    get_all_cities(all_cities, nb_user, city) # Obtenir toutes les villes des utilisateurs insrits
    city = geolocator.geocode(city) # Obtenir les coordonnées de la ville départ
    cities = {}
    for i in range(0, len(all_cities)): # Pour chaque ville dans la liste
        cities[all_cities[i]] = geolocator.geocode(all_cities[i]) # Ajout dans le dictionnaire du détail de chaque ville
        dico_city[all_cities[i]] = cities[all_cities[i]].latitude, cities[all_cities[i]].longitude # Ajout dans le dictionnaire du nom chaque ville et de ses coordonnées
        dico_city[all_cities[i]] = round(geodesic((dico_city[all_cities[i]]), (city.latitude, city.longitude)).km) # Calcul de la distance entre le point de départ et chaque ville 
    tmp = min(dico_city.values()) # Déterminer distance la plus basse à partir des valeurs
    match_city = [key for key in dico_city if dico_city[key] == tmp] # Retrouver le nom de la ville correspondante
    match_city = match_city[0]
    return match_city

def get_all_cities(all_cities, nb_user, city):
    for i in range(len(nb_user)): # Pour chaque utilisateur
            all_cities.append(nb_user[i].localisation) # Ajouter chaque ville
    all_cities.remove(city) # Enlever la ville considérée comme point de départ
    return all_cities

def get_match_gender(current_user):
    global match_sexe
    if (current_user.orientation == "Homosexuel"):
        match_sexe = current_user.sexe
    elif (current_user.sexe == 'Femme'):
        match_sexe = 'Homme'
    else:
        match_sexe = 'Femme'
    return match_sexe