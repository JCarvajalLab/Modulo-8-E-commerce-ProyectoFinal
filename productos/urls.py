from django.urls import path
from . import views

app_name = "productos" #Es para redirigir sin utilizar la url

urlpatterns = [
    path("", views.home, name="home"),
    path("productos/", views.lista_productos, name="lista_productos"),
    path("producto/<int:producto_id>/", views.detalle_producto, name="detalle_producto"),
    path("dashboard/productos/", views.panel_productos, name="panel_productos"),
    path("dashboard/productos/crear/", views.crear_producto, name="crear_producto"),
    path("dashboard/productos/editar/<int:producto_id>/", views.editar_producto, name="editar_producto"),
    path("dashboard/productos/eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar_producto"),
]