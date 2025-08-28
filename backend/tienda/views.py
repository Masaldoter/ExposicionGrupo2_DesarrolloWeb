from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto

def lista_productos(request):
    productos = list(Producto.objects.values())
    return JsonResponse(productos, safe=False)
