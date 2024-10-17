from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Marca, Proveedor, Producto, Stand, Pedido, DetallePedido, Solicitud, DetalleSolicitud, Devolucion, DetalleDevolucion
from .serializers import MarcaSerializer, ProveedorSerializer, ProductoSerializer, StandSerializer, PedidoSerializer, DetallePedidoSerializer, SolicitudSerializer, DetalleSolicitudSerializer, DevolucionSerializer, DetalleDevolucionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

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
        return Pedido.objects.filter(estado=1)
    
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
        return Solicitud.objects.filter(estado=1)

class DetalleSolicitudViewSet(viewsets.ModelViewSet):
    queryset = DetalleSolicitud.objects.all()
    serializer_class = DetalleSolicitudSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DetalleSolicitud.objects.filter(estado=1)
    
class DevolucionViewSet(viewsets.ModelViewSet):
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Devolucion.objects.filter(estado=1)

class DetalleDevolucionViewSet(viewsets.ModelViewSet):
    queryset = DetalleDevolucion.objects.all()
    serializer_class = DetalleDevolucionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DetalleDevolucion.objects.filter(estado=1)


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