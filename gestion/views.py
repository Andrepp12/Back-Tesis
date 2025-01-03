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
        return Solicitud.objects.filter(estado__in=[1, 2, 3])
    
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




 
# Diccionario para convertir números de mes a nombres de mes
MESES = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
    7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
}

@api_view(['GET'])
def cantidad_devolucion(request):
    """
    Devuelve el total de devoluciones por mes para un producto específico en un año dado,
    asegurando que la devolución y el detalle de devolución tengan estado 1, y que la devolución
    no esté relacionada con un pedido ni una solicitud.
    """
    if request.method == 'GET':
        producto_id = request.GET.get('producto_id')
        year = request.GET.get('year')

        # Validaciones básicas
        if not producto_id or not year:
            return JsonResponse({"error": "Se requieren 'producto_id' y 'year' en la solicitud."}, status=400)

        try:
            # Filtrar DetalleDevolucion con estado 1 y criterios adicionales
            devoluciones = DetalleDevolucion.objects.filter(
                estado=1,
                producto_id=producto_id,
                devolucion__estado=1,  # Asegura que la Devolucion tenga estado 1
                devolucion__fecha_devolucion__year=year,  # Año específico
                devolucion__pedido__isnull=True,  # Pedido nulo
                devolucion__solicitud__isnull=True  # Solicitud nula
            ).annotate(
                mes=ExtractMonth('devolucion__fecha_devolucion')  # Extraer el mes de la fecha de devolución
            ).values('mes').annotate(
                total_devoluciones=Count('id')  # Contar las devoluciones por mes
            ).order_by('mes')  # Ordenar por mes

            # Crear un diccionario para los resultados con nombres de mes
            resultado = {
                MESES[item['mes']]: item['total_devoluciones'] for item in devoluciones
            }

            # Devolver el total de devoluciones por mes
            return JsonResponse({'total_devoluciones_por_mes': resultado}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)



@api_view(['GET'])
def suma_razon_devolucion(request):
    """
    Devuelve la cantidad de veces que se repiten las diferentes razones de devolución,
    asegurando que la devolución y los detalles de devolución tengan estado 1.
    """
    if request.method == 'GET':
        producto_id = request.GET.get('producto_id')
        year = request.GET.get('year')

        # Validaciones básicas
        if not producto_id or not year:
            return JsonResponse({"error": "Se requieren 'producto_id' y 'year' en la solicitud."}, status=400)

        try:
            # Filtrar DetalleDevolucion con estado 1 y criterios adicionales
            devoluciones = DetalleDevolucion.objects.filter(
                estado=1,
                producto_id=producto_id,
                devolucion__estado=1,  # Asegura que la Devolucion tenga estado 1
                devolucion__fecha_devolucion__year=year,
                devolucion__pedido__isnull=True,
                devolucion__solicitud__isnull=True
            ).values('devolucion__razon').annotate(total=Count('devolucion__razon')).order_by('-total')

            # Formatear la respuesta
            suma_neta = {item['devolucion__razon']: item['total'] for item in devoluciones}
            return JsonResponse({'suma': suma_neta}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)



@api_view(['GET'])
def suma_cantidades(request):
    if request.method == 'GET':
        producto_id = request.GET.get('producto_id')
        year = request.GET.get('year')

        if not producto_id or not year:
            return JsonResponse({'error': 'Parámetros faltantes'}, status=400)

        try:
            # Filtrar y sumar cantidades de tipo_mov=1
            sumas_entradas = (
                Movimiento.objects.filter(
                    producto_id=producto_id,
                    estado=1,
                    tipo_mov=1,
                    fecha_movimiento__year=year
                )
                .annotate(month=ExtractMonth('fecha_movimiento'))  # Extraer el mes
                .values('month')
                .annotate(total_cantidad=Sum('cantidad'))  # Sumar las cantidades
                .order_by('month')
            )

            # Filtrar y sumar cantidades de tipo_mov=3
            sumas_salidas = (
                Movimiento.objects.filter(
                    producto_id=producto_id,
                    estado=1,
                    tipo_mov=3,
                    fecha_movimiento__year=year
                )
                .annotate(month=ExtractMonth('fecha_movimiento'))  # Extraer el mes
                .values('month')
                .annotate(total_cantidad=Sum('cantidad'))  # Sumar las cantidades
                .order_by('month')
            )

            # Crear un diccionario para las sumas netas por mes
            suma_neta = {}

            for entrada in sumas_entradas:
                mes = entrada['month']
                suma_neta[mes] = entrada['total_cantidad']

            for salida in sumas_salidas:
                mes = salida['month']
                if mes in suma_neta:
                    suma_neta[mes] -= salida['total_cantidad']
                else:
                    suma_neta[mes] = -salida['total_cantidad']

            # Formatear la respuesta
            return JsonResponse({'suma': suma_neta})

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
            # Filtrar y sumar cantidades de tipo_mov=1 (entradas) por año y mes
            sumas_entradas = (
                Movimiento.objects.filter(
                    producto_id=producto_id,
                    estado=1,
                    tipo_mov=1
                )
                .values(year=ExtractYear('fecha_movimiento'), month=ExtractMonth('fecha_movimiento'))  # Extraer año y mes
                .annotate(total_cantidad=Sum('cantidad'))  # Sumar las cantidades
                .order_by('year', 'month')
            )

            # Filtrar y sumar cantidades de tipo_mov=3 (salidas) por año y mes
            sumas_salidas = (
                Movimiento.objects.filter(
                    producto_id=producto_id,
                    estado=1,
                    tipo_mov=3
                )
                .values(year=ExtractYear('fecha_movimiento'), month=ExtractMonth('fecha_movimiento'))  # Extraer año y mes
                .annotate(total_cantidad=Sum('cantidad'))  # Sumar las cantidades
                .order_by('year', 'month')
            )

            # Crear un diccionario para las sumas netas por año y mes
            suma_neta = {}

            for entrada in sumas_entradas:
                year = entrada['year']
                month = entrada['month']
                if year not in suma_neta:
                    suma_neta[year] = {}
                suma_neta[year][month] = entrada['total_cantidad']

            for salida in sumas_salidas:
                year = salida['year']
                month = salida['month']
                if year not in suma_neta:
                    suma_neta[year] = {}
                if month in suma_neta[year]:
                    suma_neta[year][month] -= salida['total_cantidad']
                else:
                    suma_neta[year][month] = -salida['total_cantidad']

            # Formatear la respuesta
            return JsonResponse({'suma': suma_neta})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
def lista_productos(request):
    # Filtra los productos que tienen estado = 1
    productos = Producto.objects.filter(estado=1).select_related('marca')

    # Crea una lista de diccionarios con la información deseada, incluyendo el ID
    productos_list = [
        {
            'id': producto.id,  # Añade el ID del producto
            'nombre': producto.nombre,
            'talla': producto.talla,
            'marca': producto.marca.nombre  # Accede al nombre de la marca
        }
        for producto in productos
    ]

    return Response(productos_list)

@api_view(['GET'])
def obtener_anos_por_producto(request, producto_id):
    # Filtrar los movimientos que cumplen con las condiciones requeridas
    anos = Movimiento.objects.filter(
        producto_id=producto_id,
        estado=1,  # Estado activo
        tipo_mov=1  # Tipo de movimiento especificado
    ).annotate(
        anio=ExtractYear('fecha_movimiento')  # Extraer el año de la fecha de movimiento
    ).values('anio').distinct()  # Obtener años distintos

    # Convertir los resultados a una lista de años
    anos_list = list(anos)

    # Devolver los años en formato JSON
    return JsonResponse({'años': [a['anio'] for a in anos_list]})