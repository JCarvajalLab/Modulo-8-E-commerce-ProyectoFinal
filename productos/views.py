from django.shortcuts import render

def home(request):
    return render(request, 'productos/home.html')

def lista_productos(request):
    return render(request, 'productos/lista_productos.html')