from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lesson17.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route("/movies")
def movies():
    movies_list = [
        "Interstellar",
        "Matrix",
        "Gladiator",
        "Forrest Gump"
    ]

    return render_template(
        "movies.html",
        movies=movies_list,
        page_title="Moje ulubione filmy"
    )


@app.route("/book")
def book():
    book_data = {
        "title": "Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937
    }

    return render_template("book.html", book=book_data)


@app.route("/gallery")
def gallery():
    images = [
        {
            "url": "https://picsum.photos/id/237/300/200",
            "caption": "Pies"
        },
        {
            "url": "https://picsum.photos/id/1025/300/200",
            "caption": "Zwierzę"
        },
        {
            "url": "https://picsum.photos/id/1043/300/200",
            "caption": "Krajobraz"
        }
    ]

    return render_template("gallery.html", images=images)


@app.route("/products")
def products():
    products_list = Product.query.all()
    return render_template("products.html", products=products_list)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        registration = Registration(name=name, email=email)

        try:
            db.session.add(registration)
            db.session.commit()
            return redirect(url_for("thanks"))
        except IntegrityError:
            db.session.rollback()
            return "Taki email jest już zarejestrowany."

    return render_template("register.html")


@app.route("/thanks")
def thanks():
    return "Dziękujemy za rejestrację!"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)