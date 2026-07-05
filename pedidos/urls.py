from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('pedido/resumen/', views.confirmar_pedido, name='confirmar_pedido'),
    path('confirmar/', views.confirmar_compra, name='confirmar_compra'),
    path('pedido/<int:pedido_id>/confirmado/', views.pedido_confirmado, name='pedido_confirmado'),
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),

]