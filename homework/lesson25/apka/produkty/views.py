from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Produkt, Note, Author, Book
from .serializers import (
    ProduktSerializer,
    NoteSerializer,
    AuthorSerializer,
    BookSerializer,
)


class ProduktViewSet(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer


def set_name_view(request):
    name = request.GET.get("name")

    if not name:
        return HttpResponse(
            "Podaj imię w adresie, np. /api/set-name/?name=Anna"
        )

    response = HttpResponse(
        f"Ustawiono ciasteczko dla użytkownika: {name}"
    )
    response.set_cookie("user_name", name)

    return response


def hello_view(request):
    name = request.COOKIES.get("user_name", "Gość")

    return HttpResponse(f"Witaj, {name}!")


@api_view(["GET"])
def calculate_view(request):
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    operation = request.GET.get("operation")

    if num1 is None or num2 is None or operation is None:
        return Response(
            {
                "error": "Podaj parametry: num1, num2 oraz operation"
            },
            status=400
        )

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return Response(
            {
                "error": "Parametry num1 i num2 muszą być liczbami"
            },
            status=400
        )

    if operation == "add":
        result = num1 + num2

    elif operation == "subtract":
        result = num1 - num2

    elif operation == "multiply":
        result = num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return Response(
                {
                    "error": "Nie można dzielić przez zero"
                },
                status=400
            )

        result = num1 / num2

    else:
        return Response(
            {
                "error": (
                    "Niepoprawna operacja. "
                    "Użyj: add, subtract, multiply albo divide"
                )
            },
            status=400
        )

    return Response({
        "result": result
    })
