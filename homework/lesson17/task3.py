from flask import Flask, render_template

app = Flask(__name__)


@app.route("/movies")
def movies():
    ulubione_filmy = [
        "Interstellar",
        "Matrix",
        "Gladiator",
        "Forrest Gump"
    ]

    return render_template(
        "movies.html",
        movies=ulubione_filmy
    )


if __name__ == "__main__":
    app.run(debug=True)