from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'templates', TemplateViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]