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
    marca = MarcaSerializer(read_only=True)  # Para mostrar los detalles completos de la marca
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source='marca')  # Para permitir la asignación de la marca por su ID

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'codigo', 'descripcion', 'talla', 'precio', 'stock_almacen', 'stock_total', 'ubicacion', 'estado', 'marca', 'marca_id', 'imagen']

class StandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stand
        fields = '__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
    # pedido = PedidoSerializer()
    # producto = ProductoSerializer()
    class Meta:
        model = DetallePedido
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(read_only=True)  # Para mostrar los detalles completos de la marca
    proveedor_id = serializers.PrimaryKeyRelatedField(queryset=Proveedor.objects.all(), source='proveedor')  # Para permitir la asignación de la marca por su ID
    class Meta:
        model = Pedido
        fields = ['id', 'factura', 'fecha_pedido', 'fecha_entrega', 'precio_total', 'estado', 'proveedor', 'proveedor_id']

class SolicitudSerializer(serializers.ModelSerializer):
    stand = StandSerializer(read_only=True)
    # Utilizamos el stand_id para crear o actualizar la solicitud (solo escritura)
    stand_id = serializers.PrimaryKeyRelatedField(queryset=Stand.objects.all(), source='stand', write_only=True)

    class Meta:
        model = Solicitud
        fields = ['id', 'fecha_solicitud', 'estado', 'stand', 'stand_id']

class DetalleSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleSolicitud
        fields = '__all__'

class DevolucionSerializer(serializers.ModelSerializer):
    # Proveedor = ProveedorSerializer()
    class Meta:
        model = Devolucion
        fields = '__all__'

class DetalleDevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleDevolucion
        fields = '__all__'