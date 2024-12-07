from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100) 
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Descripción: {self.descripcion} - Precio: {self.precio} - Cantidad: {self.cantidad}"

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100) 
    direccion = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

    def __str__(self):
        return f"Nombre: {self.nombre} - Dirección: {self.direccion} - Provincia: {self.provincia}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 100 caracteres
    apellido = models.CharField(max_length=30)  # Campo string de 100 caracteres
    email = models.EmailField()
    pos_iva = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Posición IVA: {self.pos_iva}"