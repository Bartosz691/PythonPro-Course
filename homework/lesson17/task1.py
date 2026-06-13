from flask import Flask

app = Flask(__name__)


@app.route("/me")
def me():
    return "Bartosz Wypych"


if __name__ == "__main__":
    app.run(debug=True)