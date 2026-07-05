from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('pedido/resumen/', views.confirmar_pedido, name='confirmar_pedido'),
    path('confirmar/', views.confirmar_compra, name='confirmar_compra'),
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),
    path('mis-pedidos/<int:pedido_id>/',views.detalle_pedido,name='detalle_pedido'),

]