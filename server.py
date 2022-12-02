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
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)

with app.app_context():
    db.create_all()
    
@app.route("/users/create", methods=["GET", "POST"]) #pour créer son compte
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))

    return render_template("user/create.html") #tristan, faut créer la page de user_create

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
    
