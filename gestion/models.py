from django.db import models

class Marca(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    descripcion = models.TextField()
    talla =models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_almacen = models.IntegerField(default=0)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} ({self.codigo})'

class Stand(models.Model):
    ubicacion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)

class Pedido(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=50)  # Pendiente, Recibido, Cancelado

    def __str__(self):
        return f'Pedido {self.id} - {self.proveedor.nombre}'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.producto.nombre} - Cantidad: {self.cantidad}'

class Solicitud(models.Model):
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField()
    estado = models.CharField(max_length=50)  # Pendiente, Aprobada, Rechazada

    def __str__(self):
        return f'Solicitud {self.id} - {self.stand.nombre}'
    
class DetalleSolicitud(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.producto.nombre} - Cantidad: {self.cantidad}'
