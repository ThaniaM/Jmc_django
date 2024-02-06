# Generated by Django 5.0.1 on 2024-01-31 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_servicio', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'servicio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('rfc', models.CharField(blank=True, max_length=13, null=True)),
                ('cp', models.CharField(max_length=5)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
                ('id_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlCliente.servicio')),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
    ]