from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


room_equipment = db.Table(
    "room_equipment",
    db.Column("room_id", db.Integer, db.ForeignKey("rooms.id")),
    db.Column("equipment_id", db.Integer, db.ForeignKey("equipment.id"))
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    department = db.Column(db.String(50))

    is_admin = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class Equipment(db.Model):
    __tablename__ = "equipment"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    icon = db.Column(db.String(50))


class Room(db.Model):
    __tablename__ = "rooms"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    capacity = db.Column(
        db.Integer,
        nullable=False
    )

    floor = db.Column(
        db.Integer,
        default=0
    )

    description = db.Column(db.Text)

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    hourly_rate = db.Column(
        db.Numeric(10, 2),
        default=0
    )

    equipment = db.relationship(
        "Equipment",
        secondary=room_equipment,
        lazy="subquery"
    )


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    room_id = db.Column(
        db.Integer,
        db.ForeignKey("rooms.id"),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(db.Text)

    start_time = db.Column(
        db.DateTime,
        nullable=False
    )

    end_time = db.Column(
        db.DateTime,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="confirmed"
    )

    attendees_count = db.Column(
        db.Integer,
        default=1
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )