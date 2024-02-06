from django.db import models
from controlCliente.models import Servicio,Cliente


class  Equipo(models.Model):
  id_equipo = models.AutoField(primary_key=True) #Campo
  tipo_equipo  = models.CharField(max_length=45)
  procesador = models.CharField(max_length=50)
  tipo_disco = models.CharField(max_length=45)	
  uso_disco = models.CharField(max_length=15, blank=True, null=True)
  marca = models.CharField(max_length=50)
  ram = models.CharField(max_length=10)
  ip_local = models.CharField(max_length=15)
  anydesk = models.CharField(max_length=12)
  nom_usuario = models.CharField(max_length=50)
  nom_antivirus = models.CharField(max_length=20)
  vig_antivirus = models.DateField()
  office = models.CharField(max_length=30)
  vig_office = models.DateField()
  descripcion = models.TextField(max_length=600, blank=True, null=True)
  id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True)
  id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
  def save(self, *args, **kwargs):
      super(Equipo, self).save(*args, **kwargs)

  
  class Meta:
    managed = True
    db_table = 'equipo'
