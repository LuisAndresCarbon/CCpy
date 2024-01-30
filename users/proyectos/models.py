# proyectos/models.py

from django.db import models
from .queries import show_projects_query, show_catmunisig_query
from django.db import connection
from django.utils import timezone
class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=100)
    AggregationID = models.CharField(max_length=100)
    CounterpartID = models.CharField(max_length=100)
    Cve_Geo = models.CharField(max_length=100, blank=True, null=True)
    Cve_Est = models.CharField(max_length=100, blank=True, null=True)
    Cve_Mun = models.CharField(max_length=100, blank=True, null=True)
    Cve_Unica = models.CharField(max_length=100, blank=True, null=True)
    Status = models.CharField(max_length=255, default='1')
    DateCreate = models.DateTimeField(auto_now_add=True)
    IDUserCreate = models.CharField(max_length=100, blank=True, null=True)
    DateModify = models.DateTimeField(auto_now_add=True)
    IDUserModify = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = 'tb_projects'


class SigCat(models.Model): 
    CVE_GEO = models.TextField()
    CVE_EST = models.TextField()
    CVE_MUN = models.TextField()
    ESTADO = models.TextField()
    MUNICIPIO = models.TextField()

    @classmethod
    def show_all_municipal(cls):
        with connection.cursor() as cursor:
            cursor.execute(show_catmunisig_query())
            result = cursor.fetchall()

        # Mapeamos los resultados a un diccionario para seleccionar los campos específicos
        mapped_result = [{'CVE_GEO': row[0], 'CVE_EST': row[1], 'CVE_MUN': row[2], 'ESTADO': row[3], 'MUNICIPIO': row[4]} for row in result]
        return mapped_result