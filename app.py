
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


app = Flask (__name__)
app.secret_key = "supersecretkey" # Change later

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tastetracker_ps.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    reviews = db.relationships("Review", backref="author", lazy=True)

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"),nullable=False)
    restaurant_name = db.Column(db.String(100), nullable=False)
    cuisine_type = db.Column(db.String(50), nullable=False)
    review_date = db.Column(db.Date, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.Date, default=datetime.utcnow)


@app.route("/")
def home():
    reviews = Review.query.order_by(Review.created_at.desc()).all()
    return render_template("home.html", reviews=reviews)
@app.route('/reviews')
def reviews():
    query=text('SELECT * FROM reviews')
    result=connection.execute(query).fetchall()
    return render_template('reviews.html', reviews=result)
    
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists.")
            return redirect(url_for("register"))
        
        hashed_password = generate_password_has(password)

        new_user = User(
            username=username,
            email=email,
            password_hash=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully. Please log in.")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route('/logIn')
def logIn():
    return render_template('login.html')
if __name__=='__main__':
    app.run(debug=True, reloader_type='stat', port=5000)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
