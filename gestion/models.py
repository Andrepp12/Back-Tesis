from django.utils import timezone
from django.db import models

class Marca(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField(default=1)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    ruc = models.CharField(max_length=11, default='00000000000') 
    contacto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    estado = models.IntegerField(default=1)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='images/', blank=True, null=True)  # Define el valor predeterminado
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    descripcion = models.TextField()
    talla = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_almacen = models.IntegerField(default=0)
    stock_total = models.IntegerField(default=0)
    ubicacion = models.CharField(max_length=255, default="almacén")
    estado = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.nombre} ({self.codigo})'

class Stand(models.Model):
    ubicacion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField(default=1)

class ProductoStand(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    estado = models.IntegerField(default=1)

class Pedido(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    factura = models.CharField(max_length=50, default='000000')
    fecha_pedido = models.DateField( default=timezone.now)
    fecha_entrega = models.DateField( default=timezone.now )
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.IntegerField(default=1)  # Pendiente(1), Recibido(2), Cancelado(0)

    def __str__(self):
        return f'Pedido {self.id} - {self.proveedor.nombre}'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles_pedido')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.producto.nombre} - Cantidad: {self.cantidad}'

class Solicitud(models.Model):
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField()
    estado = models.IntegerField(default=1)  # Pendiente(1), Aprobada(2), Rechazada(0)

    def __str__(self):
        return f'Solicitud {self.id} - {self.stand.nombre}'
    
class DetalleSolicitud(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, related_name='detalles_solicitud')
    cantidad = models.IntegerField(default=0)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    estado = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.producto.nombre} - Cantidad: {self.cantidad}'

class Devolucion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE,  blank=True, null=True)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE,  blank=True, null=True)
    boleta = models.CharField(max_length=50,  blank=True, null=True)
    razon = models.TextField()
    descripcion = models.TextField()
    fecha_devolucion = models.DateField()
    estado = models.IntegerField(default=1)

class DetalleDevolucion(models.Model):
    devolucion = models.ForeignKey(Devolucion, on_delete=models.CASCADE, related_name='detalles_devolucion')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles_producto')
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    estado = models.IntegerField(default=1)

class TipoMovimiento(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField(default=1)
    descripcion = models.TextField()

class Movimiento(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_movimiento = models.DateField()
    codigo_trans = models.CharField(max_length=50,  blank=True, null=True)
    estado = models.IntegerField(default=1)
    tipo_mov = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE)
