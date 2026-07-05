from django.contrib import admin
from .models import Pedido, DetallePedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha', 'total',)
    ordering = ('-fecha',)

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'producto', 'cantidad', 'precio_unitario', 'subtotal',)