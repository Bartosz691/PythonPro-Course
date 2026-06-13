# sqlalchemy_app/app_orm.py

from pathlib import Path

from database import SessionLocal, engine
from models import Base, Tag, Zadanie
from sqlalchemy.orm import Session


def pokaz_zadania(db: Session):
    zadania = db.query(Zadanie).all()

    if not zadania:
        print("Brak zadań na liście.")
        return

    print("\n--- Twoja lista zadań ---")
    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        tagi = ", ".join(tag.nazwa for tag in zadanie.tagi)

        if not tagi:
            tagi = "brak"

        print(
            f"[{status}] ID: {zadanie.id}, "
            f"Opis: {zadanie.opis}, "
            f"Tagi: {tagi}"
        )

    print("------------------------\n")


def dodaj_zadanie(db: Session, opis: str):
    nowe_zadanie = Zadanie(opis=opis)
    db.add(nowe_zadanie)
    db.commit()
    db.refresh(nowe_zadanie)


def oznacz_jako_zrobione(db: Session, id_zadania: int):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()

    if zadanie:
        zadanie.zrobione = True
        db.commit()
        print("Zadanie zaktualizowane!")
    else:
        print("Nie znaleziono zadania.")


def usun_zadanie(db: Session, id_zadania: int):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()

    if zadanie:
        db.delete(zadanie)
        db.commit()
        print("Zadanie usunięte!")
    else:
        print("Nie znaleziono zadania.")


def wyszukaj_zadania(db: Session, fraza: str):
    zadania = db.query(Zadanie).filter(Zadanie.opis.contains(fraza)).all()

    if not zadania:
        print("Nie znaleziono zadań.")
        return

    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}")


def dodaj_tag_do_zadania(db: Session, id_zadania: int, nazwa_tagu: str):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()

    if not zadanie:
        print("Nie znaleziono zadania.")
        return

    tag = db.query(Tag).filter(Tag.nazwa == nazwa_tagu).first()

    if not tag:
        tag = Tag(nazwa=nazwa_tagu)
        db.add(tag)

    zadanie.tagi.append(tag)
    db.commit()

    print("Tag został dodany do zadania.")


def db_init():
    Base.metadata.create_all(bind=engine)
    print("Baza danych została zainicjalizowana.")


def main():
    if not Path("todo_orm.db").exists():
        db_init()
    else:
        Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    while True:
        print("Menu (SQLAlchemy):")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadanie po opisie")
        print("6. Dodaj tag do zadania")
        print("7. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            pokaz_zadania(db)

        elif wybor == "2":
            opis = input("Podaj opis zadania: ")
            dodaj_zadanie(db, opis)
            print("Zadanie dodane!")

        elif wybor == "3":
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                oznacz_jako_zrobione(db, id_zadania)
            except ValueError:
                print("Błędne ID.")

        elif wybor == "4":
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                usun_zadanie(db, id_zadania)
            except ValueError:
                print("Błędne ID.")

        elif wybor == "5":
            fraza = input("Podaj frazę do wyszukania: ")
            wyszukaj_zadania(db, fraza)

        elif wybor == "6":
            try:
                id_zadania = int(input("Podaj ID zadania: "))
                nazwa_tagu = input("Podaj nazwę taga: ")
                dodaj_tag_do_zadania(db, id_zadania, nazwa_tagu)
            except ValueError:
                print("Błędne ID.")

        elif wybor == "7":
            print("Do zobaczenia!")
            db.close()
            break

        else:
            print("Nieznana opcja.")


if __name__ == "__main__":
    main()
    