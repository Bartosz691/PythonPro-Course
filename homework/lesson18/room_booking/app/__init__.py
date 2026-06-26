import traceback

from flask import Flask, jsonify

from config import config
from app.models import db


def create_app(config_name="development"):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)

    from app.routes.rooms import rooms_bp
    from app.routes.bookings import bookings_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.debug import debug_bp
    from app.routes.notifications import notifications_bp
    from app.routes.reports import reports_bp

    app.register_blueprint(rooms_bp)
    app.register_blueprint(bookings_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(debug_bp)
    app.register_blueprint(notifications_bp)
    app.register_blueprint(reports_bp)

    @app.route("/")
    def index():
        return "System rezerwacji sal działa!"

    @app.route("/test-db")
    def test_db():
        try:
            db.session.execute(db.text("SELECT 1"))
            return "Połączenie OK!"
        except Exception as e:
            return f"Błąd połączenia: {e}"

    @app.errorhandler(Exception)
    def handle_exception(e):
        return jsonify({
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500

    return app