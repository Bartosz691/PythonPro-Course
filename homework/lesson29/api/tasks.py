import time
from datetime import datetime

from celery import shared_task
from django.contrib.auth.models import User
from django.utils import timezone

from .models import EmailNotification

@shared_task
def hello_world():
    print("Hello from Celery!")


@shared_task
def multiply(a, b):
    result = a * b
    print(f"Wynik mnożenia: {a} * {b} = {result}")
    return result


@shared_task
def log_timestamp():
    now = datetime.now()

    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(f"{now}\n")

    print(f"Zapisano czas: {now}")
    
    from django.contrib.auth.models import User


@shared_task
def count_users():
    count = User.objects.count()
    print(f"Liczba użytkowników w bazie: {count}")
    return count

@shared_task
def update_user_last_login(user_id):
    user = User.objects.get(id=user_id)
    user.last_login = timezone.now()
    user.save(update_fields=["last_login"])

    print(
        f"Zaktualizowano last_login użytkownika ID={user_id}: "
        f"{user.last_login}"
    )

    return user_id

@shared_task
def process_video():
    print("Rozpoczęto przetwarzanie wideo...")
    time.sleep(15)
    print("Przetwarzanie wideo zakończone.")
    return "done"

@shared_task
def send_email_notification(notification_id):
    notification = EmailNotification.objects.get(id=notification_id)

    print(f"Wysyłanie maila do: {notification.recipient_email}")

    time.sleep(5)

    notification.sent_at = timezone.now()
    notification.save(update_fields=["sent_at"])

    print(f"Mail wysłany do: {notification.recipient_email}")

    return notification.id

@shared_task(bind=True)
def progress_task(self):
    for i in range(1, 101):
        time.sleep(0.1)

        self.update_state(
            state="PROGRESS",
            meta={
                "current": i,
                "total": 100,
            },
        )

    return {
        "current": 100,
        "total": 100,
        "status": "Zakończono",
    }