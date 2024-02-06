from django.db import models
from controlCliente.models import Servicio,Cliente

class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    fecha_contrato = models.DateField(null=True, blank=True)
    vigencia_contrato = models.DateField(null=True, blank=True)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    def save(self, *args, **kwargs):
        super(Contrato, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'contrato'