import sqlite3

DATABASE_NAME = "todo_raw.db"


def init_db():
    """Inicjalizuje bazę danych i tworzy tabelę, jeśli nie istnieje."""
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


def dodaj_zadanie(opis: str, priorytet: int):
    """Dodaje nowe zadanie do bazy danych."""
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


def pobierz_zadania():
    """Pobiera wszystkie zadania z bazy danych."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, opis, zrobione, priorytet
        FROM zadania
        """)

        return cursor.fetchall()


def oznacz_jako_zrobione(id_zadania: int):
    """Oznacza zadanie o podanym ID jako zrobione."""
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


def usun_zadanie(id_zadania: int):
    """Usuwa zadanie o podanym ID."""
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


def wyszukaj_zadania(fraza: str):
    """Wyszukuje zadania, których opis zawiera podaną frazę."""
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


def edytuj_zadanie(id_zadania: int, nowy_opis: str):
    """Edytuje opis zadania o podanym ID."""
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