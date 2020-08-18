from django.contrib import admin
from django.urls import path, include

# las vistas se declaran en cada app, y luego se importan como globales

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
]
