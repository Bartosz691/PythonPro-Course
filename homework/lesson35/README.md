# Lesson 35 - Docker, Django i PostgreSQL

## Projekt

Music Fun Beats - internetowy sklep muzyczny napisany w Django i Django REST Framework.

Repozytorium projektu:

https://github.com/Bartosz691/music-fun-beats

## Zakres wykonany w ramach lekcji

W projekcie została przygotowana konfiguracja Docker Compose składająca się z:

- kontenera `web` z aplikacją Django,
- kontenera `db` z PostgreSQL 16,
- trwałego wolumenu `postgres_data`,
- healthchecka PostgreSQL,
- konfiguracji za pomocą pliku `.env`,
- pliku `.env.example` bez danych poufnych.

## Baza danych

Projekt może działać w dwóch trybach.

Lokalnie:

```text
USE_SQLITE=True