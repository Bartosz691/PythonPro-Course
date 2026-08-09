from django.http import HttpResponse

from .tasks import hello_world, multiply
from django.shortcuts import render

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