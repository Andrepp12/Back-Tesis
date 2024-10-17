from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, ProveedorViewSet, ProductoViewSet, StandViewSet, PedidoViewSet, DetallePedidoViewSet, SolicitudViewSet, DetalleSolicitudViewSet, DevolucionViewSet, DetalleDevolucionViewSet, detalles_por_pedido, detalles_por_solicitud

router = DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'stands', StandViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalles_pedido', DetallePedidoViewSet)
router.register(r'solicitudes', SolicitudViewSet)
router.register(r'detalles_solicitud', DetalleSolicitudViewSet)
router.register(r'devoluciones', DevolucionViewSet)
router.register(r'detalles_devolucion', DetalleDevolucionViewSet)

urlpatterns = [
    path('gestion/', include(router.urls)),
    path('gestion/detalles_pedido/pedido/<int:pedido_id>/', detalles_por_pedido, name='detalles_por_pedido'),
    path('gestion/detalles_solicitud/solicitud/<int:solicitud_id>/', detalles_por_solicitud, name='detalles_por_solicitud'),
]


