from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, OrderViewSet
from .views import index

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet)
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("", index, name="index"),  # Przypisz widok index do ścieżki URL
]
