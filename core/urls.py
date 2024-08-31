from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from accounts import urls as accounts_urls
from todos import urls as todos_urls


routes_lists = [
    accounts_urls.routes_list,
    todos_urls.routes_list,
]
router = routers.DefaultRouter()
for routes_list in routes_lists:
    for route in routes_list:
        router.register(route[0], route[1], basename=route[2])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
