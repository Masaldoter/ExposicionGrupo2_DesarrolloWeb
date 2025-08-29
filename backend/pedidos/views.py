from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido
from .forms import PedidoForm

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, "pedidos/lista.html", {"pedidos": pedidos})

def crear_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, "pedidos/crear.html", {"form": form})

def editar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, "pedidos/editar_pedido.html", {"form": form})

def cancelar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.estado = "Cancelado"
    pedido.save()
    return redirect('lista_pedidos')

def entregar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.estado = "Entregado"
    pedido.save()
    return redirect('lista_pedidos')
