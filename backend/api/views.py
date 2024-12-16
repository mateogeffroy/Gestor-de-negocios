from rest_framework import viewsets
from .serializer import ProductoSerializer, ProveedorSerializer, VentaSerializer, VentaDetalleSerializer, CajaSerializer
from .models import Producto, Proveedor, Venta, VentaDetalle, Caja

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaDetalleViewSet(viewsets.ModelViewSet):
    queryset = VentaDetalle.objects.all()
    serializer_class = VentaDetalleSerializer

class CajaViewSet(viewsets.ModelViewSet):
    queryset = Caja.objects.all()
    serializer_class = CajaSerializer