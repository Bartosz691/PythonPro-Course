
from django.urls import path
from rest_framework import routers


from .views import (
    ProduktViewSet,
    NoteViewSet,
    set_name_view,
    hello_view,
    calculate_view
)

router = routers.DefaultRouter()
router.register(r"produkty", ProduktViewSet)
router.register(r"notes", NoteViewSet)

urlpatterns = [
    path("set-name/", set_name_view),
    path("hello/", hello_view),
    path("calculate/", calculate_view),
]

urlpatterns += router.urls