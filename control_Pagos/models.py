from django.db import models
from controlCliente .models import Servicio,Cliente

class Pago(models.Model):
  id_pago =  models.AutoField(primary_key=True)
  fecha = models.DateField(null=True, blank=True)
  pdf = models.TextField(null=True, blank=True)
  total_pago = models.CharField(null=True, blank=True, max_length=50)
  id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True)
  id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
  def save(self, *args, **kwargs):
        super(Pago, self).save(*args, **kwargs)

  class Meta:
      managed = True
      db_table = 'pago'
