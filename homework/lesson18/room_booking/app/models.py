from datetime import datetime
from sqlalchemy import event
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

    room = db.relationship(
        "Room",
        backref="bookings"
    )

    user = db.relationship(
        "User",
        backref="bookings"
    )


class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    message = db.Column(
        db.String(255),
        nullable=False
    )

    is_read = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user = db.relationship(
        "User",
        backref="notifications"
    )


@event.listens_for(Booking, "after_insert")
def create_admin_notification(mapper, connection, target):
    users_table = User.__table__
    notifications_table = Notification.__table__

    admins = connection.execute(
        users_table.select().where(users_table.c.is_admin == True)
    ).fetchall()

    for admin in admins:
        connection.execute(
            notifications_table.insert().values(
                user_id=admin.id,
                message=f"Utworzono nową rezerwację: {target.title}",
                is_read=False,
                created_at=datetime.utcnow()
            )
        )