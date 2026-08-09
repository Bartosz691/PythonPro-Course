from datetime import datetime

from celery import shared_task

from django.contrib.auth.models import User


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