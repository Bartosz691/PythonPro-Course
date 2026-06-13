from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///registrations.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        registration = Registration(
            name=name,
            email=email
        )

        db.session.add(registration)
        db.session.commit()

        return redirect(url_for("thanks"))

    return render_template("register.html")


@app.route("/thanks")
def thanks():
    return "Dziękujemy za rejestrację!"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)