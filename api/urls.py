from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'items', ItemViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'templates', TemplateViewSet)


urlpatterns = [
    path('', api_root, name="root"),
    path('v1/', include(router.urls)),
]


