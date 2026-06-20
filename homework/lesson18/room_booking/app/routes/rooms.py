from flask import Blueprint, jsonify

rooms_bp = Blueprint(
    "rooms",
    __name__,
    url_prefix="/api/rooms"
)


@rooms_bp.route("/")
def get_rooms():
    return jsonify({
        "message": "Lista sal"
    })