# Generated by Django 5.0.6 on 2024-10-29 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_alter_producto_talla'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='genero',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
