from django.http import HttpResponse

from django.shortcuts import render
from .tasks import hello_world, multiply, process_video

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