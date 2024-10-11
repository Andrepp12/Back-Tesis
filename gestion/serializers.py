from rest_framework import serializers
from .models import Marca, Proveedor, Producto, Stand, Pedido, DetallePedido, Solicitud, DetalleSolicitud, Devolucion, DetalleDevolucion

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()
    class Meta:
        model = Producto
        fields = '__all__'

class StandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stand
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    # detalles = serializers.StringRelatedField(many=True)
    proveedor = ProveedorSerializer()
    class Meta:
        model = Pedido
        fields = '__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer()
    producto = ProductoSerializer()
    class Meta:
        model = DetallePedido
        fields = '__all__'

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'

class DetalleSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleSolicitud
        fields = '__all__'

class DevolucionSerializer(serializers.ModelSerializer):
    Proveedor = ProveedorSerializer()
    class Meta:
        model = Devolucion
        fields = '__all__'

class DetalleDevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleDevolucion
        fields = '__all__'