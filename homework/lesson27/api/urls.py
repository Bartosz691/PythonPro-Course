from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import ProductViewSet


router = DefaultRouter()

router.register(
    "products",
    ProductViewSet,
    basename="product",
)


urlpatterns = [
    path("cached/", views.cached_view),
    path("selective/", views.selective_cache_view),
    path("", include(router.urls)),
]