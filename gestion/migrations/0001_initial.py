# Generated by Django 5.1 on 2024-12-20 13:38

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.CharField(default='000000', max_length=50)),
                ('fecha_pedido', models.DateField(default=django.utils.timezone.now)),
                ('fecha_entrega', models.DateField(default=django.utils.timezone.now)),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ruc', models.CharField(default='00000000000', max_length=11)),
                ('contacto', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField()),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.IntegerField(default=1)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boleta', models.CharField(blank=True, max_length=50, null=True)),
                ('razon', models.TextField()),
                ('descripcion', models.TextField()),
                ('fecha_devolucion', models.DateField()),
                ('estado', models.IntegerField(default=1)),
                ('pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.pedido')),
                ('solicitud', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('codigo', models.CharField(max_length=50)),
                ('genero', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField()),
                ('talla', models.DecimalField(decimal_places=1, max_digits=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_almacen', models.IntegerField(default=0)),
                ('stock_total', models.IntegerField(default=0)),
                ('ubicacion', models.CharField(default='almacén', max_length=255)),
                ('estado', models.IntegerField(default=1)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.marca')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.IntegerField(default=1)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_pedido', to='gestion.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleDevolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('estado', models.IntegerField(default=1)),
                ('devolucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_devolucion', to='gestion.devolucion')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_producto', to='gestion.producto')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.proveedor'),
        ),
        migrations.CreateModel(
            name='DetalleSolicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('estado', models.IntegerField(default=1)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_solicitud', to='gestion.solicitud')),
            ],
        ),
        migrations.AddField(
            model_name='solicitud',
            name='stand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.stand'),
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha_movimiento', models.DateField()),
                ('codigo_trans', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.IntegerField(default=1)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
                ('stand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.stand')),
                ('tipo_mov', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.tipomovimiento')),
            ],
        ),
    ]
