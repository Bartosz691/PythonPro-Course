from django.urls import path

from . import views


urlpatterns = [
    path("cached/", views.cached_view, name="cached_view"),
    path(
        "selective/",
        views.selective_cache_view,
        name="selective_cache",
    ),
]