import sqlite3

DATABASE_NAME = "todo_raw.db"


class TaskManagerRaw:
    def __init__(self):
        self.init_db()

    def init_db(self):
        """Inicjalizuje bazę danych."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS zadania (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                opis TEXT NOT NULL,
                priorytet INTEGER DEFAULT 1,
                zrobione BOOLEAN NOT NULL DEFAULT 0 CHECK (zrobione IN (0, 1))
            )
            """)

            conn.commit()

    def dodaj(self, opis: str, priorytet: int):
        """Dodaje zadanie."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO zadania (opis, priorytet, zrobione)
                VALUES (?, ?, ?)
                """,
                (opis, priorytet, False)
            )

            conn.commit()

    def pobierz(self):
        """Pobiera wszystkie zadania."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute("""
            SELECT id, opis, zrobione, priorytet
            FROM zadania
            """)

            return cursor.fetchall()

    def oznacz_jako_zrobione(self, id_zadania: int):
        """Oznacza zadanie jako zrobione."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE zadania
                SET zrobione = ?
                WHERE id = ?
                """,
                (True, id_zadania)
            )

            conn.commit()

    def usun(self, id_zadania: int):
        """Usuwa zadanie."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM zadania
                WHERE id = ?
                """,
                (id_zadania,)
            )

            conn.commit()

    def wyszukaj(self, fraza: str):
        """Wyszukuje zadania po opisie."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT id, opis, zrobione, priorytet
                FROM zadania
                WHERE opis LIKE ?
                """,
                (f"%{fraza}%",)
            )

            return cursor.fetchall()

    def edytuj(self, id_zadania: int, nowy_opis: str):
        """Edytuje opis zadania."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE zadania
                SET opis = ?
                WHERE id = ?
                """,
                (nowy_opis, id_zadania)
            )

            conn.commit()


def pokaz_liste_zadan(zadania):
    if not zadania:
        print("Brak zadań na liście.")
        return

    print("\n--- Twoja lista zadań ---")
    for zadanie in zadania:
        status = "✓" if zadanie[2] else "✗"
        print(
            f"[{status}] ID: {zadanie[0]}, "
            f"Opis: {zadanie[1]}, "
            f"Priorytet: {zadanie[3]}"
        )
    print("------------------------\n")


def main():
    manager = TaskManagerRaw()

    while True:
        print("Menu klasowe Raw SQL:")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadanie")
        print("6. Edytuj zadanie")
        print("7. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            pokaz_liste_zadan(manager.pobierz())

        elif wybor == "2":
            opis = input("Podaj opis zadania: ")

            try:
                priorytet = int(input("Podaj priorytet: "))
            except ValueError:
                print("Błędny priorytet. Ustawiono 1.")
                priorytet = 1

            manager.dodaj(opis, priorytet)
            print("Zadanie dodane!")

        elif wybor == "3":
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                manager.oznacz_jako_zrobione(id_zadania)
                print("Zadanie zaktualizowane!")
            except ValueError:
                print("Błędne ID.")

        elif wybor == "4":
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                manager.usun(id_zadania)
                print("Zadanie usunięte!")
            except ValueError:
                print("Błędne ID.")

        elif wybor == "5":
            fraza = input("Podaj frazę do wyszukania: ")
            pokaz_liste_zadan(manager.wyszukaj(fraza))

        elif wybor == "6":
            try:
                id_zadania = int(input("Podaj ID zadania do edycji: "))
                nowy_opis = input("Podaj nowy opis zadania: ")
                manager.edytuj(id_zadania, nowy_opis)
                print("Zadanie edytowane!")
            except ValueError:
                print("Błędne ID.")

        elif wybor == "7":
            print("Do zobaczenia!")
            break

        else:
            print("Nieznana opcja.")


if __name__ == "__main__":
    main()