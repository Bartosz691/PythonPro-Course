from celery.result import AsyncResult
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import transaction
from .models import UploadedImage
from .models import UploadedImage, TransactionItem
from celery import chain

from .tasks import (
    generate_users_csv,
    hello_world,
    multiply,
    process_video,
    progress_task,
    classify_uploaded_image,
    generate_random_number,
    multiply_by_ten,
    save_chain_result,
    process_transaction_item,
)


def hello_celery(request):
    hello_world.delay()

    return HttpResponse("Zadanie Celery zostało wysłane.")


def multiply_view(request):
    if request.method == "POST":
        a = int(request.POST.get("a"))
        b = int(request.POST.get("b"))

        multiply.delay(a, b)

        return HttpResponse(
            "Zadanie mnożenia zostało wysłane do Celery."
        )

    return render(request, "multiply.html")


def process_video_view(request):
    process_video.delay()

    return HttpResponse("Przetwarzanie wideo rozpoczęte!")


def start_progress_task(request):
    task = progress_task.delay()

    return JsonResponse({
        "task_id": task.id
    })


def task_status(request, task_id):
    task = AsyncResult(task_id)

    response = {
        "task_id": task_id,
        "state": task.state,
    }

    if task.state == "PROGRESS":
        response["current"] = task.info.get("current", 0)
        response["total"] = task.info.get("total", 100)

    elif task.state == "SUCCESS":
        response["current"] = 100
        response["total"] = 100
        response["result"] = task.result

    return JsonResponse(response)


def generate_report_view(request):
    task = generate_users_csv.delay()

    return JsonResponse({
        "task_id": task.id
    })


def report_status_view(request, task_id):
    task = AsyncResult(task_id)

    response = {
        "task_id": task_id,
        "state": task.state,
    }

    if task.state == "SUCCESS":
        file_name = task.result

        response["download_url"] = request.build_absolute_uri(
            f"/media/{file_name}"
        )

    return JsonResponse(response)

def upload_image_view(request):
    if request.method == "POST":
        image_file = request.FILES.get("image")

        uploaded = UploadedImage.objects.create(
            image=image_file
        )

        task = classify_uploaded_image.delay(uploaded.id)

        return JsonResponse({
            "image_id": uploaded.id,
            "task_id": task.id,
            "message": "Obraz zapisany i wysłany do klasyfikacji.",
        })

    return render(request, "upload_image.html")

def start_chain_view(request):
    workflow = chain(
        generate_random_number.s(),
        multiply_by_ten.s(),
        save_chain_result.s(),
    )

    task = workflow.apply_async()

    return JsonResponse({
        "task_id": task.id,
        "message": "Łańcuch zadań Celery został uruchomiony.",
    })
    
def transaction_test_view(request):
    with transaction.atomic():
        item = TransactionItem.objects.create(
            name="Obiekt testowy"
        )

        transaction.on_commit(
            lambda: process_transaction_item.delay(item.id)
        )

    return JsonResponse({
        "item_id": item.id,
        "message": "Obiekt utworzono, zadanie Celery uruchomiono po commit.",
    })