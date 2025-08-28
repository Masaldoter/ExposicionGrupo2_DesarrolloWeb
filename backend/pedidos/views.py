from django.shortcuts import render, redirect
from .models import Pedido
from .forms import PedidoForm

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/lista.html', {'pedidos': pedidos})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/crear.html', {'form': form})
