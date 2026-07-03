from rest_framework import routers

from .views import ProduktViewSet

router = routers.DefaultRouter()
router.register(r'produkty', ProduktViewSet)

urlpatterns = router.urls