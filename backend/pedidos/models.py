from django.db import models

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.producto} ({self.cantidad})"
