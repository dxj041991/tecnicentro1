# Generated by Django 3.0.4 on 2020-08-01 00:00

import core.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('Cedula', models.CharField(max_length=10, unique=True)),
                ('NombreCliente', models.CharField(max_length=30)),
                ('Apellidos', models.CharField(max_length=30)),
                ('Telefono', models.CharField(max_length=10)),
                ('Direccion', models.CharField(max_length=30)),
                ('Estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('precioVenta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precioCompra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('observaciones', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id_vehiculo', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=10)),
                ('modelo', models.CharField(max_length=30)),
                ('client', models.ForeignKey(on_delete=core.models.Cliente, to='core.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('kilo', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('descr', models.CharField(max_length=20)),
                ('veh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='detVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cant', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Venta')),
            ],
        ),
    ]
