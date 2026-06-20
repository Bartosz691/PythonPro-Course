from flask import Blueprint, jsonify

bookings_bp = Blueprint(
    "bookings",
    __name__,
    url_prefix="/api/bookings"
)


@bookings_bp.route("/")
def get_bookings():
    return jsonify({
        "message": "Lista rezerwacji"
    })