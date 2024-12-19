from rest_framework import serializers
from .models import Marca, Movimiento, Proveedor, Producto, Stand, Pedido, DetallePedido, Solicitud, DetalleSolicitud, Devolucion, DetalleDevolucion, TipoMovimiento

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
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source='marca', write_only=True)  # Para permitir la asignación de la marca por su ID

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'codigo', 'descripcion', 'talla', 'precio', 'genero', 'color', 'stock_almacen', 'stock_total', 'ubicacion', 'estado', 'marca', 'marca_id', 'imagen']

class StandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stand
        fields = '__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    # Utilizamos el stand_id para crear o actualizar la solicitud (solo escritura)
    producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='producto', write_only=True)

    class Meta:
        model = DetallePedido
        fields = ['id', 'pedido', 'cantidad', 'precio_unitario', 'estado', 'producto', 'producto_id']


class PedidoSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(read_only=True)  # Para mostrar los detalles completos de la marca
    proveedor_id = serializers.PrimaryKeyRelatedField(queryset=Proveedor.objects.all(), source='proveedor', write_only=True)  # Para permitir la asignación de la marca por su ID
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
    producto = ProductoSerializer(read_only=True)
    # Utilizamos el stand_id para crear o actualizar la solicitud (solo escritura)
    producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='producto', write_only=True)

    class Meta:
        model = DetalleSolicitud
        fields = ['id', 'solicitud', 'cantidad', 'estado', 'producto', 'producto_id']


class DevolucionSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer(read_only=True)  # Para mostrar los detalles completos del pedido
    pedido_id = serializers.PrimaryKeyRelatedField(
        queryset=Pedido.objects.all(), source='pedido', write_only=True, required=False
    )  # Para permitir la asignación del pedido por su ID, no requerido
    solicitud = SolicitudSerializer(read_only=True)  # Para mostrar los detalles completos de la solicitud
    solicitud_id = serializers.PrimaryKeyRelatedField(
        queryset=Solicitud.objects.all(), source='solicitud', write_only=True, required=False
    )  # Para permitir la asignación de la solicitud por su ID, no requerido

    class Meta:
        model = Devolucion
        fields = ['id', 'boleta', 'solicitud', 'solicitud_id', 'razon', 'descripcion', 'fecha_devolucion', 'estado', 'pedido', 'pedido_id']

class DetalleDevolucionSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    # Utilizamos el stand_id para crear o actualizar la solicitud (solo escritura)
    producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='producto', write_only=True)

    class Meta:
        model = DetalleDevolucion
        fields = ['id', 'devolucion', 'cantidad', 'descripcion', 'estado', 'producto', 'producto_id']

class TipoMovimientoSerializer(serializers.ModelSerializer):
    # producto = ProductoSerializer(read_only=True)
    # # Utilizamos el stand_id para crear o actualizar la solicitud (solo escritura)
    # producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='producto', write_only=True)

    class Meta:
        model = TipoMovimiento
        fields = '__all__'

class MovimientoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    # # Utilizamos el stand_id para crear o actualizar la solicitud (solo escritura)
    producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='producto', write_only=True)

    tipo_mov = TipoMovimientoSerializer(read_only=True)  # Para mostrar los detalles completos de la solicitud
    tipo_mov_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoMovimiento.objects.all(), source='tipo_mov', write_only=True, required=False
    )  # Para permitir la asignación de la solicitud por su ID, no requerido

    class Meta:
        model = Movimiento
        fields = ['id', 'cantidad', 'fecha_movimiento', 'codigo_trans', 'estado', 'stand', 'tipo_mov', 'tipo_mov_id', 'producto', 'producto_id']