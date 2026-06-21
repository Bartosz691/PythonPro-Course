from datetime import datetime, timedelta

from flask import Blueprint, jsonify

from app.models import db, Booking, Notification

notifications_bp = Blueprint(
    "notifications",
    __name__,
    url_prefix="/api/notifications"
)


def create_upcoming_booking_reminders():
    now = datetime.now()
    one_hour_later = now + timedelta(hours=1)

    bookings = Booking.query.filter(
        Booking.status == "confirmed",
        Booking.start_time >= now,
        Booking.start_time <= one_hour_later
    ).all()

    for booking in bookings:
        message = (
            f"Przypomnienie: rezerwacja '{booking.title}' "
            f"rozpoczyna się za mniej niż 1 godzinę."
        )

        existing_notification = Notification.query.filter_by(
            user_id=booking.user_id,
            message=message
        ).first()

        if not existing_notification:
            notification = Notification(
                user_id=booking.user_id,
                message=message
            )

            db.session.add(notification)

    db.session.commit()


@notifications_bp.route("/", methods=["GET"])
def get_unread_notifications():
    create_upcoming_booking_reminders()

    notifications = Notification.query.filter_by(
        is_read=False
    ).order_by(
        Notification.created_at.desc()
    ).all()

    return jsonify([
        {
            "id": notification.id,
            "user_id": notification.user_id,
            "message": notification.message,
            "is_read": notification.is_read,
            "created_at": notification.created_at.isoformat()
        }
        for notification in notifications
    ])


@notifications_bp.route("/<int:notification_id>/read", methods=["POST"])
def mark_notification_as_read(notification_id):
    notification = Notification.query.get_or_404(notification_id)

    notification.is_read = True
    db.session.commit()

    return jsonify({
        "message": "Powiadomienie oznaczone jako przeczytane",
        "notification_id": notification.id
    })