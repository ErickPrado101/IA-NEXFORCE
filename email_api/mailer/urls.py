from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmailViewSet

router = DefaultRouter()
router.register(r'emails', EmailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
