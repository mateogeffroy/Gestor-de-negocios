from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('producto', views.ProductoViewSet)
router.register('proveedor', views.ProveedorViewSet)
router.register('venta', views.VentaViewSet)
router.register('ventas_detalle', views.VentaDetalleViewSet)
router.register('caja', views.CajaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]