# proyectos/models.py

from django.db import models

class Estado(models.Model):
    idEstado = models.TextField(primary_key=True)
    nomEstado = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_estado'

class aggregation(models.Model):
    idaggregation = models.TextField(primary_key=True)
    descripcion = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_aggregation'