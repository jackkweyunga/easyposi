from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'bussiness', BussinessViewSet)

urlpatterns = [
    path('api/', api_root, name="root"),
    path('api/v1/', include(router.urls)),
]


