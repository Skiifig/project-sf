from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # création extension
app = Flask(__name__) # creation app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db" # configure SQLite database
db.init_app(app) # initialise l'app avec l'extension

@app.route('/')
def index():
    return render_template('index.html')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String, unique=True)
    lname = db.Column(db.String unique=True)
    email = db.Column(db.String)
    password = db.Column(db.String)

with app.app_context():
    db.create_all()
    
@app.route("/inscription", methods=["GET", "POST"]) #pour créer son compte
def user_create():
    if request.method == "POST":
        user = User(
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()
        return redirect("user_detail", id=user.id)

    return render_template("registration.html") #tristan, faut créer la page de user_create

@app.route("/dashboard")
def user_detail(id):
    user = db.get_or_404(User, id)
    return render_template("dashboard.html", user=user)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
    
