from django import urls
from django.urls import path, include
from .views import PenulisanViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('penulisan', PenulisanViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]