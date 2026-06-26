from io import BytesIO
from datetime import datetime

from flask import Blueprint, send_file
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from sqlalchemy.orm import joinedload

from app.models import Booking

reports_bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/api/reports"
)


@reports_bp.route("/bookings/pdf", methods=["GET"])
def export_bookings_pdf():
    buffer = BytesIO()

    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 50

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "Raport rezerwacji sal")

    y -= 30

    pdf.setFont("Helvetica", 10)
    pdf.drawString(
        50,
        y,
        f"Data wygenerowania: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    y -= 40

    bookings = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).order_by(
        Booking.start_time.asc()
    ).all()

    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, y, "ID")
    pdf.drawString(80, y, "Tytul")
    pdf.drawString(230, y, "Sala")
    pdf.drawString(330, y, "Uzytkownik")
    pdf.drawString(450, y, "Start")

    y -= 15

    pdf.setFont("Helvetica", 9)

    for booking in bookings:
        if y < 50:
            pdf.showPage()
            y = height - 50
            pdf.setFont("Helvetica", 9)

        pdf.drawString(50, y, str(booking.id))
        pdf.drawString(80, y, booking.title[:22])
        pdf.drawString(230, y, booking.room.name[:15])
        pdf.drawString(330, y, booking.user.name[:18])
        pdf.drawString(
            450,
            y,
            booking.start_time.strftime("%Y-%m-%d %H:%M")
        )

        y -= 15

    pdf.save()

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="raport_rezerwacji.pdf",
        mimetype="application/pdf"
    )
