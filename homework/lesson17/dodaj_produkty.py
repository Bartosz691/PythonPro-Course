from app import app, db, Product

with app.app_context():

    p1 = Product(
        name="Laptop",
        price=3500.00
    )

    p2 = Product(
        name="Telefon",
        price=1800.00
    )

    p3 = Product(
        name="Klawiatura",
        price=250.00
    )

    db.session.add_all([
        p1,
        p2,
        p3
    ])

    db.session.commit()

    print("Produkty zostały dodane.")