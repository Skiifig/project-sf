from flask import Blueprint, render_template, request, redirect, url_for
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

@main.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@main.route('/confirmation', methods=['POST'])
def confirmation_post():
    user = User.query.filter_by(email=current_user.email).first()
    user.sexe = request.form.get("sexe")
    user.localisation = request.form.get("localisation")
    user.orientation = request.form.get("orientation")
    db.session.commit()
    return redirect(url_for("auth.login"))


@main.route('/profile')
@login_required
def profile():
    return render_template('dashboard.html', name=current_user.fname)

@main.route('/settings')
@login_required
def settings():
    return render_template('settings.html', user=current_user)