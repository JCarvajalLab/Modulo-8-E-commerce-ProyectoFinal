from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('carrito/', views.ver_carrito, name='ver_carrito'),
]