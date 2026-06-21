import time

from flask import Blueprint, jsonify
from sqlalchemy import event
from sqlalchemy.orm import joinedload

from app.models import db, Booking

debug_bp = Blueprint(
    "debug",
    __name__,
    url_prefix="/debug"
)

query_count = 0
listener_registered = False


def register_query_counter():
    global listener_registered

    if listener_registered:
        return

    @event.listens_for(db.engine, "before_cursor_execute")
    def count_queries(conn, cursor, statement, parameters, context, executemany):
        global query_count
        query_count += 1

    listener_registered = True


@debug_bp.route("/n-plus-1")
def debug_n_plus_1():
    global query_count

    register_query_counter()

    query_count = 0
    start_time = time.time()

    bookings = Booking.query.all()

    without_optimization_data = []

    for booking in bookings:
        without_optimization_data.append({
            "title": booking.title,
            "room": booking.room.name,
            "user": booking.user.name
        })

    without_optimization_time = time.time() - start_time
    without_optimization_queries = query_count

    query_count = 0
    start_time = time.time()

    optimized_bookings = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).all()

    with_optimization_data = []

    for booking in optimized_bookings:
        with_optimization_data.append({
            "title": booking.title,
            "room": booking.room.name,
            "user": booking.user.name
        })

    with_optimization_time = time.time() - start_time
    with_optimization_queries = query_count

    return jsonify({
        "without_optimization": {
            "description": "Wersja bez optymalizacji - problem N+1",
            "query_count": without_optimization_queries,
            "execution_time_seconds": without_optimization_time,
            "data": without_optimization_data
        },
        "with_optimization": {
            "description": "Wersja z joinedload",
            "query_count": with_optimization_queries,
            "execution_time_seconds": with_optimization_time,
            "data": with_optimization_data
        },
        "summary": {
            "saved_queries": without_optimization_queries - with_optimization_queries
        }
    })