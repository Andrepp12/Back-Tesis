# Generated by Django 5.0.6 on 2024-10-01 04:28

import django.db.models.deletion
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
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateField()),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField()),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('talla', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_almacen', models.IntegerField(default=0)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.marca')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='gestion.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
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
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='gestion.solicitud')),
            ],
        ),
        migrations.AddField(
            model_name='solicitud',
            name='stand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.stand'),
        ),
    ]
