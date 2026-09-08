# Lesson 37 - Celery, Redis i zadania okresowe

## Projekt

Music Fun Beats - internetowy sklep muzyczny napisany w Django i Django REST Framework.

Repozytorium projektu:

https://github.com/Bartosz691/music-fun-beats

## Zakres

Do projektu została dodana obsługa zadań asynchronicznych za pomocą Celery.

Docker Compose zawiera:

- Django,
- PostgreSQL,
- Redis,
- worker `celery_orders`,
- worker `celery_notifications`,
- Celery Beat.

## Redis

Redis jest wykorzystywany jako:

- DB 0 - broker Celery,
- DB 1 - cache Django,
- DB 2 - backend wyników Celery.

## Kolejki

Projekt posiada dwie kolejki:

- `orders`
- `notifications`

Worker `celery_orders` obsługuje kolejkę `orders`.

Worker `celery_notifications` obsługuje kolejkę `notifications`.

## Zadania

### check_low_stock

Sprawdza aktywne albumy z niskim stanem magazynowym.

Celery Beat uruchamia zadanie automatycznie co 60 sekund.

### process_order

Przetwarza informacje dotyczące zamówienia.

### send_order_notification

Generuje powiadomienie dotyczące utworzonego zamówienia i kodu płatności.

## Celery Beat

Celery Beat pełni rolę schedulera zadań okresowych.

Co minutę wysyła:

`products.tasks.check_low_stock`

do kolejki:

`orders`

## Weryfikacja

Sprawdzono:

- dwa działające workery,
- dwie różne kolejki,
- działający Redis broker,
- działający Celery Beat,
- wykonanie zadania `check_low_stock`,
- wykonanie zadania `send_order_notification`.

## Testy

Cały projekt w środowisku Docker + PostgreSQL przechodzi:

```text
16 passed