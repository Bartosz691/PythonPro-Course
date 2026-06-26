import uuid
from datetime import datetime
import traceback

from dateutil.rrule import rrule, WEEKLY, MONTHLY
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import joinedload

from app.models import db, Booking, Room, User

print("WCZYTANO NOWY BOOKINGS.PY")

bookings_bp = Blueprint(
    "bookings",
    __name__,
    url_prefix="/api/bookings"
)


@bookings_bp.route("/", methods=["GET"])
def get_bookings():
    bookings = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).order_by(
        Booking.start_time.desc()
    ).all()

    return jsonify([
        {
            "id": booking.id,
            "title": booking.title,
            "room": booking.room.name,
            "user": booking.user.name,
            "start_time": booking.start_time.isoformat(),
            "end_time": booking.end_time.isoformat(),
            "status": booking.status,
            "attendees_count": booking.attendees_count,
            "recurrence_rule": booking.recurrence_rule,
            "series_id": booking.series_id
        }
        for booking in bookings
    ])


@bookings_bp.route("/recurring", methods=["POST"])
def create_recurring_booking():
    try:
        data = request.get_json()

        required = [
            "room_id",
            "user_id",
            "title",
            "start_time",
            "end_time",
            "recurrence_rule",
            "count"
        ]

        for field in required:
            if field not in data:
                return jsonify({
                    "error": f"Brak wymaganego pola: {field}"
                }), 400

        try:
            start_time = datetime.fromisoformat(data["start_time"])
            end_time = datetime.fromisoformat(data["end_time"])
        except ValueError:
            return jsonify({
                "error": "Niepoprawny format daty ISO"
            }), 400

        if start_time >= end_time:
            return jsonify({
                "error": "Czas rozpoczęcia musi być przed czasem zakończenia"
            }), 400

        room = Room.query.get(data["room_id"])

        if not room:
            return jsonify({
                "error": "Sala nie istnieje"
            }), 404

        user = User.query.get(data["user_id"])

        if not user:
            return jsonify({
                "error": "Użytkownik nie istnieje"
            }), 404

        duration = end_time - start_time
        recurrence_rule = data["recurrence_rule"]

        if recurrence_rule == "WEEKLY":
            frequency = WEEKLY
        elif recurrence_rule == "MONTHLY":
            frequency = MONTHLY
        else:
            return jsonify({
                "error": "Nieobsługiwana reguła. Użyj WEEKLY albo MONTHLY."
            }), 400

        try:
            count = int(data["count"])
        except ValueError:
            return jsonify({
                "error": "Pole count musi być liczbą całkowitą"
            }), 400

        if count <= 0:
            return jsonify({
                "error": "Pole count musi być większe od 0"
            }), 400

        series_id = str(uuid.uuid4())

        occurrences = list(
            rrule(
                freq=frequency,
                dtstart=start_time,
                count=count
            )
        )

        conflicts = []

        for occurrence_start in occurrences:
            occurrence_end = occurrence_start + duration

            if not room.is_available(occurrence_start, occurrence_end):
                conflicts.append({
                    "start_time": occurrence_start.isoformat(),
                    "end_time": occurrence_end.isoformat()
                })

        if conflicts:
            return jsonify({
                "error": "Wykryto konflikty dla części rezerwacji",
                "conflicts": conflicts
            }), 409

        created_bookings = []

        for occurrence_start in occurrences:
            occurrence_end = occurrence_start + duration

            booking = Booking(
                room_id=room.id,
                user_id=user.id,
                title=data["title"],
                description=data.get("description"),
                start_time=occurrence_start,
                end_time=occurrence_end,
                attendees_count=data.get("attendees_count", 1),
                recurrence_rule=recurrence_rule,
                series_id=series_id
            )

            db.session.add(booking)
            created_bookings.append(booking)

        db.session.commit()

        return jsonify({
            "message": "Utworzono serię rezerwacji",
            "series_id": series_id,
            "created_count": len(created_bookings),
            "bookings": [
                {
                    "id": booking.id,
                    "title": booking.title,
                    "start_time": booking.start_time.isoformat(),
                    "end_time": booking.end_time.isoformat()
                }
                for booking in created_bookings
            ]
        }), 201

    except Exception as e:
        db.session.rollback()

        return jsonify({
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500


@bookings_bp.route("/series/<string:series_id>", methods=["DELETE"])
def cancel_booking_series(series_id):
    bookings = Booking.query.filter_by(
        series_id=series_id
    ).all()

    if not bookings:
        return jsonify({
            "error": "Nie znaleziono serii rezerwacji"
        }), 404

    for booking in bookings:
        booking.status = "cancelled"

    db.session.commit()

    return jsonify({
        "message": "Anulowano całą serię rezerwacji",
        "series_id": series_id,
        "cancelled_count": len(bookings)
    })


@bookings_bp.route("/<int:booking_id>", methods=["DELETE"])
def cancel_single_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)

    booking.status = "cancelled"
    db.session.commit()

    return jsonify({
        "message": "Anulowano pojedynczą rezerwację",
        "booking_id": booking.id
    })