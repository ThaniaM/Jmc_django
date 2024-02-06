from django.db import models
from django.contrib.auth.models import AbstractUser

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=80)

    class Meta:
        managed = True
        db_table = 'servicio'

class Cliente(AbstractUser):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    correo = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    rfc = models.CharField(max_length=13, null=True, blank=True)
    cp = models.CharField(max_length=5)
    estado = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=30, default='', unique=True)
    password = models.CharField(max_length=15)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, default=1)

    class Meta:
        managed = True
        db_table = 'cliente'