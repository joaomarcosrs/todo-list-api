from django.urls import path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'register', views.ResgisterViewSet, basename='register')

urlpatterns = router.urls