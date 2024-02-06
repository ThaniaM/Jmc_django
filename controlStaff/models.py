from django.db import models

class Staff(models.Model):
    id_staff = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    departamento = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=80, null=True, blank=True)
    password = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'staff'

    def __str__(self):
        return self.nombre
    
