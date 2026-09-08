# Lesson 38 - CI, GitHub Actions i pre-commit

## Projekt

Music Fun Beats - internetowy sklep muzyczny napisany w Django i Django REST Framework.

Repozytorium projektu:

https://github.com/Bartosz691/music-fun-beats

## Zakres wykonany w ramach lekcji

Do projektu została dodana automatyczna kontrola jakości kodu.

Wykorzystane zostały:

- GitHub Actions,
- pytest,
- Django system check,
- pre-commit.

## Pre-commit

Pre-commit uruchamia testy przed utworzeniem lokalnego commita.

Konfiguracja zawiera hook:

```text
python -m pytest -q