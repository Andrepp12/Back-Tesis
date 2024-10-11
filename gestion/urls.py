from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, ProveedorViewSet, ProductoViewSet, StandViewSet, PedidoViewSet, DetallePedidoViewSet, SolicitudViewSet, DetalleSolicitudViewSet, DevolucionViewSet, DetalleDevolucionViewSet

router = DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'stands', StandViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalles_pedido', DetallePedidoViewSet)
router.register(r'solicitudes', SolicitudViewSet)
router.register(r'detalles_solicituf', DetalleSolicitudViewSet)
router.register(r'devoluciones', DevolucionViewSet)
router.register(r'detalles_devolucion', DetalleDevolucionViewSet)

urlpatterns = [
    path('gestion/', include(router.urls)),
]
