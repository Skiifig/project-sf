from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # création extension

def create_app():
    app = Flask(__name__) # creation app

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db" # configure SQLite database

    db.init_app(app) # initialise l'app avec l'extension

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app