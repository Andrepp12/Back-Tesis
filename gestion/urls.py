from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, MovimientoViewSet, ProveedorViewSet, ProductoViewSet, StandViewSet, PedidoViewSet, DetallePedidoViewSet, SolicitudViewSet, DetalleSolicitudViewSet, DevolucionViewSet, DetalleDevolucionViewSet, TipoMovimientoViewSet, detalles_por_devolucion, detalles_por_pedido, detalles_por_solicitud, listar_devoluciones_con_boleta, listar_devoluciones_con_pedido, listar_devoluciones_con_solicitud, suma_cantidad_all
from .views import suma_cantidades
from .views import lista_anios
from .views import obtener_meses_por_año
from .views import obtener_productos_por_año

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
router.register(r'tipo_movimiento', TipoMovimientoViewSet)
router.register(r'movimientos', MovimientoViewSet)

urlpatterns = [
    path('gestion/', include(router.urls)),
    path('gestion/detalles_pedido/pedido/<int:pedido_id>/', detalles_por_pedido, name='detalles_por_pedido'),
    path('gestion/detalles_solicitud/solicitud/<int:solicitud_id>/', detalles_por_solicitud, name='detalles_por_solicitud'),
    path('gestion/detalles_devolucion/devolucion/<int:devolucion_id>/', detalles_por_devolucion, name='detalles_por_devolucion'),
    path('gestion/devoluciones-con-solicitud/', listar_devoluciones_con_solicitud, name='devoluciones-con-solicitud'),
    path('gestion/devoluciones-con-pedido/', listar_devoluciones_con_pedido, name='devoluciones-con-pedido'),
    path('gestion/devoluciones-con-boleta/', listar_devoluciones_con_boleta, name='devoluciones-con-boleta'),
    
    path('gestion/suma-cantidades/', suma_cantidades, name='suma_cantidades'),
    path('gestion/anos/', lista_anios, name='lista_anios'),
    path('gestion/meses/<int:año>/', obtener_meses_por_año, name='obtener_meses_por_año'),
    path('gestion/productos/ano/<int:año>/', obtener_productos_por_año, name='obtener_productos_por_año'),
    path('gestion/suma-cantidades-all/', suma_cantidad_all, name='suma_cantidad_all'),
]


