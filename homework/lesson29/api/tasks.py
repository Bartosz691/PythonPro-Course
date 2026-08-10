import time
from datetime import datetime

from celery import shared_task
from django.contrib.auth.models import User
from django.utils import timezone
from .models import EmailNotification, LogEntry, ScrapedPage
from datetime import timedelta
import requests
from bs4 import BeautifulSoup

import csv
from pathlib import Path
from django.conf import settings


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
    
@shared_task
def cleanup_old_logs():
    cutoff_date = timezone.now() - timedelta(days=90)

    deleted_count, _ = LogEntry.objects.filter(
        created_at__lt=cutoff_date
    ).delete()

    print(f"Usunięto starych wpisów LogEntry: {deleted_count}")

    return deleted_count

@shared_task
def scrape_example_title():
    url = "https://example.com"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string.strip()

    page = ScrapedPage.objects.create(
        url=url,
        title=title,
    )

    print(f"Pobrano tytuł strony: {title}")

    return page.id

@shared_task
def generate_users_csv():
    media_dir = Path(settings.MEDIA_ROOT)
    media_dir.mkdir(parents=True, exist_ok=True)

    file_name = "users_report.csv"
    file_path = media_dir / file_name

    users = User.objects.all()

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "id",
            "username",
            "email",
        ])

        for user in users:
            writer.writerow([
                user.id,
                user.username,
                user.email,
            ])

    print(f"Wygenerowano raport CSV: {file_path}")

    return file_name