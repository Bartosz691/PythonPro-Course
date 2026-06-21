from datetime import datetime, timedelta

from flask import Blueprint, render_template, jsonify
from sqlalchemy import func, desc
from sqlalchemy.orm import joinedload

from app.models import db, Room, Booking, User

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():
    now = datetime.now()

    stats = {
        "total_rooms": Room.query.filter_by(is_active=True).count(),
        "total_users": User.query.count(),
        "total_bookings": Booking.query.filter_by(status="confirmed").count(),
        "bookings_today": Booking.query.filter(
            func.date(Booking.start_time) == datetime.today().date(),
            Booking.status == "confirmed"
        ).count()
    }

    upcoming = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).filter(
        Booking.start_time >= now,
        Booking.start_time <= now + timedelta(hours=24),
        Booking.status == "confirmed"
    ).order_by(Booking.start_time).limit(10).all()

    top_users = db.session.query(
        User.name,
        func.count(Booking.id).label("booking_count")
    ).join(Booking).filter(
        Booking.status != "cancelled"
    ).group_by(User.id).order_by(desc("booking_count")).limit(5).all()

    # 1. Wykres kołowy - rozkład rezerwacji per departament
    department_stats = db.session.query(
        User.department,
        func.count(Booking.id).label("booking_count")
    ).join(Booking).filter(
        Booking.status != "cancelled"
    ).group_by(User.department).all()

    department_labels = [
        row.department or "Brak działu"
        for row in department_stats
    ]

    department_values = [
        row.booking_count
        for row in department_stats
    ]

    # 2. Heatmapa - dzień tygodnia x godzina
    heatmap_query = db.session.query(
        func.extract("dow", Booking.start_time).label("weekday"),
        func.extract("hour", Booking.start_time).label("hour"),
        func.count(Booking.id).label("booking_count")
    ).filter(
        Booking.status != "cancelled"
    ).group_by(
        "weekday",
        "hour"
    ).all()

    weekdays = ["Nd", "Pn", "Wt", "Śr", "Cz", "Pt", "Sb"]
    hours = list(range(8, 19))

    heatmap_data = {
        day: {
            hour: 0
            for hour in hours
        }
        for day in weekdays
    }

    for row in heatmap_query:
        weekday_index = int(row.weekday)
        hour = int(row.hour)

        if hour in hours:
            day_name = weekdays[weekday_index]
            heatmap_data[day_name][hour] = row.booking_count

    max_heatmap_value = 1

    for day in heatmap_data.values():
        for count in day.values():
            if count > max_heatmap_value:
                max_heatmap_value = count

    # 3. Trend - liczba rezerwacji dziennie w ostatnich 30 dniach
    start_date = now.date() - timedelta(days=29)

    trend_query = db.session.query(
        func.date(Booking.start_time).label("booking_date"),
        func.count(Booking.id).label("booking_count")
    ).filter(
        Booking.status != "cancelled",
        Booking.start_time >= start_date
    ).group_by(
        "booking_date"
    ).order_by(
        "booking_date"
    ).all()

    trend_dict = {
        str(row.booking_date): row.booking_count
        for row in trend_query
    }

    trend_labels = []
    trend_values = []

    for i in range(30):
        day = start_date + timedelta(days=i)
        day_text = str(day)

        trend_labels.append(day_text)
        trend_values.append(trend_dict.get(day_text, 0))

    return render_template(
        "dashboard.html",
        stats=stats,
        upcoming=upcoming,
        top_users=top_users,
        department_labels=department_labels,
        department_values=department_values,
        weekdays=weekdays,
        hours=hours,
        heatmap_data=heatmap_data,
        max_heatmap_value=max_heatmap_value,
        trend_labels=trend_labels,
        trend_values=trend_values
    )


@dashboard_bp.route("/api/dashboard/stats")
def api_stats():
    return jsonify({
        "rooms": Room.query.count(),
        "users": User.query.count(),
        "bookings": Booking.query.count(),
    })