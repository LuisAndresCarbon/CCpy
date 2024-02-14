# proyectos/models.py

from django.db import models
from django.core.exceptions import ValidationError
class Project(models.Model):
    ProjectID       = models.AutoField(primary_key=True)
    Folio_proyect   = models.CharField(max_length=100, blank=True)
    ProjectName     = models.CharField(max_length=100)
    AggregationID   = models.CharField(max_length=100)
    CounterpartID   = models.CharField(max_length=100)
    Cve_Geo         = models.CharField(max_length=100, blank=True, null=True)
    Cve_Est         = models.CharField(max_length=100, blank=True, null=True)
    Cve_Mun         = models.CharField(max_length=100, blank=True, null=True)
    id_phin         = models.CharField(max_length=100)
    Cve_Unica       = models.CharField(max_length=100, blank=True, null=True)
    Tipo       = models.CharField(max_length=100, blank=True, null=True)
    Status          = models.CharField(max_length=255, default='1', blank=True,)
    DateCreate      = models.DateTimeField(auto_now_add=True)
    IDUserCreate    = models.CharField(max_length=100, blank=True, null=True)
    DateModify      = models.DateTimeField(blank=True)
    IDUserModify    = models.CharField(max_length=100, blank=True, null=True)
    def clean(self):
        # Validar si alguno de los campos requeridos
        required_fields = ['ProjectName', 'AggregationID', 'CounterpartID']
        for field in required_fields:
            if not getattr(self, field, None):
                raise ValidationError(f'El campo "{field}" es requerido')
    class Meta:
        db_table = 'tb_projects'

class Aggregation(models.Model):
    ID_Agregation = models.AutoField(primary_key=True)
    AgregationID = models.TextField()
    class Meta:
        db_table = 'ct_agregationid'
    
class Estado(models.Model):
    idEstado = models.TextField(primary_key=True)
    nomEstado = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_estado'
    

class Municipio(models.Model):
    Id_municipio = models.AutoField(primary_key=True)
    Id_estado = models.IntegerField()
    clave_municipio = models.CharField(max_length=10)
    nombre_municipio = models.CharField(max_length=255)
    tb_estados = models.ForeignKey(Estado, on_delete=models.CASCADE, db_column='tb_estados_Id_estado')
    class Meta:
        db_table = 'tb_municipios'


class GeoNucleo(models.Model):
    Id_Proyecto = models.AutoField(primary_key=True)
    CVE_UNICA  = models.TextField()
    CVE_GEO  = models.TextField()
    NOM_NUC  = models.TextField()
    clavegeonucleo_Id_clave_geo_nucleo = models.ForeignKey(Estado, on_delete=models.CASCADE, db_column='tb_estados_Id_estado')
    class Meta:
        db_table = 'nucleoclavegeorelacion'

    