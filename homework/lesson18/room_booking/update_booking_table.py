from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    db.session.execute(db.text("""
        ALTER TABLE bookings
        ADD COLUMN IF NOT EXISTS recurrence_rule VARCHAR(30);
    """))

    db.session.execute(db.text("""
        ALTER TABLE bookings
        ADD COLUMN IF NOT EXISTS series_id VARCHAR(36);
    """))

    db.session.commit()

    print("Tabela bookings została zaktualizowana.")