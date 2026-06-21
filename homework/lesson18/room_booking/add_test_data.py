from datetime import datetime, timedelta

from app import create_app
from app.models import db, User, Room, Equipment, Booking

app = create_app()

with app.app_context():
    if User.query.count() == 0:
        users = [
            User(name="Jan Kowalski", email="jan@test.pl", department="IT"),
            User(name="Anna Nowak", email="anna@test.pl", department="HR"),
            User(name="Piotr Wiśniewski", email="piotr@test.pl", department="Sprzedaż"),
        ]
        db.session.add_all(users)

    if Equipment.query.count() == 0:
        equipment = [
            Equipment(name="Projektor", icon="projector"),
            Equipment(name="TV", icon="tv"),
            Equipment(name="Tablica", icon="board"),
        ]
        db.session.add_all(equipment)

    db.session.commit()

    if Room.query.count() == 0:
        rooms = [
            Room(name="Sala A", capacity=10, floor=1, description="Mała sala konferencyjna"),
            Room(name="Sala B", capacity=20, floor=2, description="Średnia sala konferencyjna"),
            Room(name="Sala C", capacity=40, floor=3, description="Duża sala konferencyjna"),
        ]
        db.session.add_all(rooms)
        db.session.commit()

    if Booking.query.count() == 0:
        users = User.query.all()
        rooms = Room.query.all()

        start = datetime.now().replace(minute=0, second=0, microsecond=0) + timedelta(days=1)

        bookings = [
            Booking(
                title="Spotkanie zespołu",
                room_id=rooms[0].id,
                user_id=users[0].id,
                start_time=start,
                end_time=start + timedelta(hours=1),
                attendees_count=5,
            ),
            Booking(
                title="Rozmowa rekrutacyjna",
                room_id=rooms[1].id,
                user_id=users[1].id,
                start_time=start + timedelta(hours=2),
                end_time=start + timedelta(hours=3),
                attendees_count=3,
            ),
            Booking(
                title="Prezentacja projektu",
                room_id=rooms[2].id,
                user_id=users[2].id,
                start_time=start + timedelta(hours=4),
                end_time=start + timedelta(hours=6),
                attendees_count=15,
            ),
        ]

        db.session.add_all(bookings)
        db.session.commit()

    print("Dane testowe wraz z rezerwacjami zostały dodane.")