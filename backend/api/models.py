from django.db import models

class Producto(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=100)
    codigoDeBarras = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    idProveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateField()
    total = models.FloatField()

    def __str__(self):
        return self.fecha
    
class VentaDetalle(models.Model):
    cantidad = models.IntegerField()
    precio = models.FloatField()
    idVenta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE)

    def __str__(self):
        return self.cantidad

class Caja(models.Model):
    fecha = models.DateField()
    total = models.FloatField()
    estado = models.BooleanField()
    idVenta = models.ForeignKey('Venta', on_delete=models.CASCADE)

    def __str__(self):
        return f'Caja del dia {self.fecha}'
    