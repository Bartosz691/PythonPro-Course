# Lesson 33 - testy projektu Music Fun Beats

Zadanie zostało wykonane w ramach projektu końcowego Music Fun Beats
napisanego w Django i Django REST Framework.

Pełne repozytorium projektu:
https://github.com/Bartosz691/music-fun-beats

## Zakres testów

Testy obejmują:

- serializery Django REST Framework,
- własną logikę biznesową w warstwie services,
- endpointy REST API,
- modele Django i testową bazę danych,
- fixtures oraz Factory Boy.

## Pliki

### test_serializers.py

Testuje walidację danych wejściowych, między innymi:

- poprawne dane koszyka,
- odrzucenie `quantity = 0`.

### test_services.py

Testuje własną logikę biznesową aplikacji:

- zwiększanie ilości produktu już znajdującego się w koszyku,
- blokowanie zakupu powyżej dostępnego stanu magazynowego,
- limit zakupu edycji limitowanej,
- tworzenie zamówienia,
- zapis historycznej ceny produktu,
- ponowne sprawdzenie stanu magazynowego podczas checkoutu.

### test_api.py

Testy integracyjne sprawdzają przepływ:

API endpoint -> View -> Serializer -> Service -> Model -> testowa baza danych

Sprawdzane są między innymi:

- dodanie albumu do koszyka,
- HTTP 409 Conflict przy niewystarczającym stanie magazynowym,
- utworzenie zamówienia,
- wygenerowanie kodu płatności,
- wyczyszczenie koszyka po checkout,
- zmniejszenie stanu magazynowego.

### factories.py

Zawiera fabryki danych testowych wykorzystujące Factory Boy.

## Technologie testowe

- pytest
- pytest-django
- pytest-mock
- Factory Boy
- Faker

## Wynik

Aktualny zestaw testów projektu:

10 passed