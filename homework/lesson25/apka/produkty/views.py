from django.http import HttpResponse
from rest_framework import viewsets

from .models import Produkt, Note
from .serializers import ProduktSerializer, NoteSerializer


class ProduktViewSet(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


def set_name_view(request):
    name = request.GET.get("name")

    if not name:
        return HttpResponse("Podaj imię w adresie, np. /api/set-name/?name=Anna")

    response = HttpResponse(f"Ustawiono ciasteczko dla użytkownika: {name}")
    response.set_cookie("user_name", name)

    return response


def hello_view(request):
    name = request.COOKIES.get("user_name", "Gość")

    return HttpResponse(f"Witaj, {name}!")