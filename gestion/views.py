from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Marca, Movimiento, Proveedor, Producto, Stand, Pedido, DetallePedido, Solicitud, DetalleSolicitud, Devolucion, DetalleDevolucion, TipoMovimiento
from .serializers import MarcaSerializer, MovimientoSerializer, ProveedorSerializer, ProductoSerializer, StandSerializer, PedidoSerializer, DetallePedidoSerializer, SolicitudSerializer, DetalleSolicitudSerializer, DevolucionSerializer, DetalleDevolucionSerializer, TipoMovimientoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from .services import obtener_suma_cantidades  # Ajusta la ruta según sea necesario
from .services import obtener_anios
from django.db.models import Count
from django.utils import timezone
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db.models import Sum, F
from django.db.models.functions import ExtractYear, ExtractMonth

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Marca.objects.filter(estado=1)
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        marca = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        marca.estado = 0
        marca.save()
        return Response({"detail": "Marca marcada como inactiva"}, status=status.HTTP_204_NO_CONTENT)

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Proveedor.objects.filter(estado=1)
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        proveedor = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        proveedor.estado = 0
        proveedor.save()
        return Response({"detail": "Proveedor marcado como inactivo"}, status=status.HTTP_204_NO_CONTENT)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Producto.objects.filter(estado=1)
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        producto = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        producto.estado = 0
        producto.save()
        return Response({"detail": "Producto marcado como inactivo"}, status=status.HTTP_204_NO_CONTENT)

class StandViewSet(viewsets.ModelViewSet):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Stand.objects.filter(estado=1)
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        stand = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        stand.estado = 0
        stand.save()
        return Response({"detail": "Stand marcado como inactivo"}, status=status.HTTP_204_NO_CONTENT)

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Pedido.objects.filter(estado__in=[1, 2])
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        pedido = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        pedido.estado = 0
        pedido.save()
        return Response({"detail": "Pedido marcado como inactivo"}, status=status.HTTP_204_NO_CONTENT)

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DetallePedido.objects.filter(estado=1)
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        detallePedido = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        detallePedido.estado = 0
        detallePedido.save()
        return Response({"detail": "DetallePedido marcado como inactivo"}, status=status.HTTP_204_NO_CONTENT)

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Solicitud.objects.filter(estado__in=[1, 2])
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        solicitud = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        solicitud.estado = 0
        solicitud.save()
        return Response({"detail": "solicitud marcada como inactivo"}, status=status.HTTP_204_NO_CONTENT)

class DetalleSolicitudViewSet(viewsets.ModelViewSet):
    queryset = DetalleSolicitud.objects.all()
    serializer_class = DetalleSolicitudSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DetalleSolicitud.objects.filter(estado=1)
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        detalleSolicitud = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        detalleSolicitud.estado = 0
        detalleSolicitud.save()
        return Response({"detail": "detalleSolicitud marcada como inactivo"}, status=status.HTTP_204_NO_CONTENT)
    
class DevolucionViewSet(viewsets.ModelViewSet):
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Devolucion.objects.filter(estado=1)
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        devolucion = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        devolucion.estado = 0
        devolucion.save()
        return Response({"detail": "devolucion marcada como inactivo"}, status=status.HTTP_204_NO_CONTENT)

class DetalleDevolucionViewSet(viewsets.ModelViewSet):
    queryset = DetalleDevolucion.objects.all()
    serializer_class = DetalleDevolucionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DetalleDevolucion.objects.filter(estado=1)
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        detalledevolucion = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        detalledevolucion.estado = 0
        detalledevolucion.save()
        return Response({"detail": "detalledevolucion marcada como inactivo"}, status=status.HTTP_204_NO_CONTENT)

class TipoMovimientoViewSet(viewsets.ModelViewSet):
    queryset = TipoMovimiento.objects.all()
    serializer_class = TipoMovimientoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TipoMovimiento.objects.filter(estado=1)
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        tipo_mov = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        tipo_mov.estado = 0
        tipo_mov.save()
        return Response({"detail": "tipo movimiento marcada como inactivo"}, status=status.HTTP_204_NO_CONTENT)
    
class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Movimiento.objects.filter(estado=1)
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el objeto a eliminar (cambiar estado)
        movimiento = self.get_object()
        # Cambiar el estado a 0 en lugar de eliminar el objeto
        movimiento.estado = 0
        movimiento.save()
        return Response({"detail": "Movimiento marcada como inactivo"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def detalles_por_pedido(request, pedido_id):
    try:
        # Filtrar los detalles por pedido
        detalles = DetallePedido.objects.filter(pedido_id=pedido_id)
        # Serializar los detalles
        serializer = DetallePedidoSerializer(detalles, many=True)
        return Response(serializer.data)
    except DetallePedido.DoesNotExist:
        return Response({"detail": "No se encontraron detalles para este pedido."}, status=404)
    
@api_view(['GET'])
def detalles_por_solicitud(request, solicitud_id):
    try:
        # Filtrar los detalles por solicitud
        detalles = DetalleSolicitud.objects.filter(solicitud_id=solicitud_id)
        # Serializar los detalles
        serializer = DetalleSolicitudSerializer(detalles, many=True)
        return Response(serializer.data)
    except DetalleSolicitud.DoesNotExist:
        return Response({"detail": "No se encontraron detalles para esta solicitud."}, status=404)
    
@api_view(['GET'])
def detalles_por_devolucion(request, devolucion_id):
    try:
        # Filtrar los detalles por devolucion
        detalles = DetalleDevolucion.objects.filter(devolucion_id=devolucion_id)
        # Serializar los detalles
        serializer = DetalleDevolucionSerializer(detalles, many=True)
        return Response(serializer.data)
    except DetalleDevolucion.DoesNotExist:
        return Response({"detail": "No se encontraron detalles para esta devolucion."}, status=404)
    
@api_view(['GET'])
def listar_devoluciones_con_solicitud(request):
    # Filtrar las devoluciones donde 'solicitud' no es null
    devoluciones = Devolucion.objects.filter(solicitud__isnull=False)
    
    # Serializar los datos
    serializer = DevolucionSerializer(devoluciones, many=True)
    
    # Retornar la respuesta JSON con las devoluciones filtradas
    return Response(serializer.data)

@api_view(['GET'])
def listar_devoluciones_con_pedido(request):
    # Filtrar las devoluciones donde 'pedido' no es null
    devoluciones = Devolucion.objects.filter(pedido__isnull=False)
    
    # Serializar los datos
    serializer = DevolucionSerializer(devoluciones, many=True)
    
    # Retornar la respuesta JSON con las devoluciones filtradas
    return Response(serializer.data)

@api_view(['GET'])
def listar_devoluciones_con_boleta(request):
    # Filtrar las devoluciones donde 'pedido' no es null
    devoluciones = Devolucion.objects.filter(boleta__isnull=False)
    
    # Serializar los datos
    serializer = DevolucionSerializer(devoluciones, many=True)
    
    # Retornar la respuesta JSON con las devoluciones filtradas
    return Response(serializer.data)


@api_view(['GET'])
def suma_cantidades(request):
    if request.method == 'GET':
        producto_id = request.GET.get('producto_id')
        year = request.GET.get('year')  # Cambiar 'año' a 'year'

        if not producto_id or not year:
            return JsonResponse({'error': 'Parámetros faltantes'}, status=400)

        try:
            # Sumar las cantidades agrupadas por mes
            resultados = (
                DetalleSolicitud.objects.filter(
                    producto_id=producto_id,
                    estado=1,
                    solicitud__estado=2,
                    solicitud__fecha_solicitud__year=year
                )
                .values(month=ExtractMonth('solicitud__fecha_solicitud'))  # Extraer el mes
                .annotate(total_cantidad=Sum('cantidad'))  # Sumar las cantidades
                .order_by('month')  # Ordenar por mes
            )

            # Formatear la respuesta
            suma = {result['month']: result['total_cantidad'] for result in resultados}

            return JsonResponse({'suma': suma})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        

@api_view(['GET'])
def lista_anios(request):
    anios = obtener_anios()
    anios_list = [anio['fecha_solicitud__year'] for anio in anios]
    return Response(anios_list)

@api_view(['GET'])
def obtener_meses_por_año(request, año):
    try:
        # Filtra las solicitudes por el año seleccionado y obtiene los meses
        meses = Solicitud.objects.filter(
            estado=2,
            fecha_solicitud__year=año
        ).values('fecha_solicitud__month').annotate(count=Count('id')).order_by('fecha_solicitud__month')

        # Extrae los meses únicos
        meses_unicos = [mes['fecha_solicitud__month'] for mes in meses]
        
        return JsonResponse({'meses': meses_unicos}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@api_view(['GET'])
def obtener_productos_por_año(request, año):
    productos = DetalleSolicitud.objects.filter(
        estado=1,
        solicitud__estado=2,
        solicitud__fecha_solicitud__year=año
    ).values('producto__id', 'producto__nombre', 'producto__talla').distinct()

    # Convierte los resultados a una lista de diccionarios
    productos_list = list(productos)

    return JsonResponse({'productos': productos_list})

@api_view(['GET'])
def suma_cantidad_all(request):
    if request.method == 'GET':
        producto_id = request.GET.get('producto_id')

        if not producto_id:
            return JsonResponse({'error': 'Parámetro "producto_id" faltante'}, status=400)

        try:
            # Sumar las cantidades agrupadas por año y mes
            resultados = (
                DetalleSolicitud.objects.filter(
                    producto_id=producto_id,
                    estado=1,
                    solicitud__estado=2
                )
                .values(year=ExtractYear('solicitud__fecha_solicitud'), month=ExtractMonth('solicitud__fecha_solicitud'))  # Extraer año y mes
                .annotate(total_cantidad=Sum('cantidad'))  # Sumar las cantidades
                .order_by('year', 'month')  # Ordenar por año y mes
            )

            # Formatear la respuesta
            suma = {}
            for result in resultados:
                year = result['year']
                month = result['month']
                if year not in suma:
                    suma[year] = {}
                suma[year][month] = result['total_cantidad']

            return JsonResponse({'suma': suma})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
