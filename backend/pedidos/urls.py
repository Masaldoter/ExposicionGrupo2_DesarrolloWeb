from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),
    path('crear/', views.crear_pedido, name='crear_pedido'),
    path('editar/<int:id>/', views.editar_pedido, name='editar_pedido'),
    path('cancelar/<int:id>/', views.cancelar_pedido, name='cancelar_pedido'),
    path('entregar/<int:id>/', views.entregar_pedido, name='entregar_pedido'),
]
