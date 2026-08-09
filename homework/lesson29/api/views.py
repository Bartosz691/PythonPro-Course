from django.http import HttpResponse, JsonResponse


from django.shortcuts import render
from .tasks import hello_world, multiply, process_video,  progress_task
from celery.result import AsyncResult


def hello_celery(request):
    hello_world.delay()

    return HttpResponse("Zadanie Celery zostało wysłane.")

def multiply_view(request):
    if request.method == "POST":
        a = int(request.POST.get("a"))
        b = int(request.POST.get("b"))

        multiply.delay(a, b)

        return HttpResponse("Zadanie mnożenia zostało wysłane do Celery.")

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