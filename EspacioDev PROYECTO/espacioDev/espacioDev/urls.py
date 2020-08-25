from django.contrib import admin
from django.urls import path, include

from core import views
from portfolio import views
from blog import views

# las vistas se declaran en cada app, y luego se importan como globales

urlpatterns = [
    path("", include("core.urls")),
    path("", include("portfolio.urls")),
    path("", include("blog.urls")),
    path("admin/", admin.site.urls),
]
