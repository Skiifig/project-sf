from os.path import join, dirname, realpath
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask

db = SQLAlchemy() # Création de la base de données

def create_app():
    app = Flask(__name__) # Création de l'application

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuop1'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db" # Définition du chemin et du nom de la base de données
    app.config["UPLOAD_FOLDER"] = join(dirname(realpath(__file__)), 'static/images/') # Définition du chemin d'enregistrement des photos de profils

    db.init_app(app) # initialise l'app avec l'extension

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # importation des routes de auth.py
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # importation des routes de main.py
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app