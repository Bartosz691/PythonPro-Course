
from django.urls import path

from . import views


urlpatterns = [
    path("hello/", views.hello_celery),
    path("multiply/", views.multiply_view),
]