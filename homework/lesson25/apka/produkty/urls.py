from django.urls import path
from rest_framework import routers

from .views import (
    ProduktViewSet,
    NoteViewSet,
    AuthorViewSet,
    BookViewSet,
    set_name_view,
    hello_view,
    calculate_view,
)


router = routers.DefaultRouter()
router.register(r"produkty", ProduktViewSet)
router.register(r"notes", NoteViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)

urlpatterns = [
    path("set-name/", set_name_view),
    path("hello/", hello_view),
    path("calculate/", calculate_view),
]

urlpatterns += router.urls
