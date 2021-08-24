from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'items', ItemViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = [
    path('api/', api_root, name="root"),
    path('api/v1/', include(router.urls)),
]


