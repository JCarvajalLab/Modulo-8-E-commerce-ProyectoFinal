from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre","disponible",)
    list_filter = ("disponible",)
    search_fields = ("nombre",)
    ordering = ("nombre",)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock", "categoria", "disponible",)
    list_filter = ("disponible", "categoria",)
    search_fields = ("nombre", "descripcion",)