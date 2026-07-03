from django.urls import path
from . import views

app_name = "productos" #Es para redirigir sin utilizar la url

urlpatterns = [
    path("", views.home, name="home"),
    path("productos/", views.lista_productos, name="lista_productos"),
]