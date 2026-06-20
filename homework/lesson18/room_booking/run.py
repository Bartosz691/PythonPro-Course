from app import create_app
from app.models import db

app = create_app()

print("Zarejestrowane trasy:")
print(app.url_map)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=False, use_reloader=False, port=5050)