from django.shortcuts import render

from django.http import HttpResponse


def ver_carrito(request):
    return HttpResponse('Carrito de compras')
