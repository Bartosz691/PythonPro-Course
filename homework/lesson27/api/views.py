import time

from django.core.cache import cache
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer


@cache_page(60)
def cached_view(request):
    return JsonResponse(
        {
            "message": "Odpowiedź została wygenerowana.",
            "timestamp": time.time(),
        }
    )


def selective_cache_view(request):
    szybkie_dane = {
        "liczba_uzytkownikow": 10
    }

    wynik_obliczen = cache.get("complex_calculation")

    if wynik_obliczen is None:
        time.sleep(3)

        wynik_obliczen = {
            "wynik": 123456,
            "z_cache": False,
        }

        cache.set(
            "complex_calculation",
            wynik_obliczen,
            60,
        )
    else:
        wynik_obliczen["z_cache"] = True

    return JsonResponse(
        {
            "szybkie_dane": szybkie_dane,
            "skomplikowane_obliczenia": wynik_obliczen,
        }
    )


@method_decorator(cache_page(600), name="list")
@method_decorator(cache_page(60), name="retrieve")
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        product = serializer.save()

        cache.clear()

        return product