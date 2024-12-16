from django.contrib import admin
from .models import Producto, Proveedor, Venta, VentaDetalle, Caja

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Venta)
admin.site.register(VentaDetalle)   
admin.site.register(Caja)