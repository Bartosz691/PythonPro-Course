# Lesson 36 - Redis i cache Django

## Projekt

Music Fun Beats - internetowy sklep muzyczny napisany w Django i Django REST Framework.

Repozytorium projektu:

https://github.com/Bartosz691/music-fun-beats

## Zakres wykonany w ramach lekcji

Do projektu został dodany Redis używany jako backend cache Django.

Środowisko Docker Compose zawiera obecnie:

- Django,
- PostgreSQL,
- Redis.

## Redis

Redis działa jako osobny kontener:

```text
redis:7-alpine