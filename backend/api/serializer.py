from rest_framework import serializers
from .models import Producto, Proveedor, Venta, VentaDetalle, Caja

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

class VentaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaDetalle
        fields = '__all__'

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = '__all__'