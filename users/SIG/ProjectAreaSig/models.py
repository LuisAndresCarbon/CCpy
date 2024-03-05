
from django.db import models

class Areaproject(models.Model):
    idareadeproyecto = models.IntegerField(primary_key=True)
    IdProject = models.IntegerField()
    Idcertificacion = models.IntegerField()
    SuperficieTotalPhina = models.TextField()
    Achurado = models.TextField()
    Expopriado = models.TextField()
    LinkPHINA = models.TextField()
    SuperficieTotal = models.TextField()
    IdsolicitudRAN = models.IntegerField()
    SuperficiePlanoInterno = models.TextField()
    AreasExpropiadas = models.TextField()
    AñodelPlan = models.TextField()
    LinkPlanoInterno = models.TextField()
    IdStatusValidacionAP = models.IntegerField()
    ObservacionesAP = models.TextField()
    LinkAP = models.TextField()
    IdLeadSIG = models.IntegerField()

    class Meta:
        db_table = 'tb_areadeproyecto'

class CatalogRequestalRan(models.Model):
    IdsolicitudRAN = models.IntegerField(primary_key=True)
    SolictiudalRAM = models.IntegerField()
    class Meta:
        db_table = 'ct_solicitudalran'

class Catalogcertificacion(models.Model):
    Idcertificacion = models.IntegerField(primary_key=True)
    Certificacion = models.IntegerField()
    class Meta:
        db_table = 'ct_certificacion'

class Catalogstatusvalidacionap(models.Model):
    IdStatusValidacionAP = models.IntegerField(primary_key=True)
    StatusValicionAP = models.IntegerField()
    class Meta:
        db_table = 'ct_statusvalidacionap'

class Catalogleadsig(models.Model):
    IdLeadSIG = models.IntegerField(primary_key=True)
    LeadSIG = models.IntegerField()
    class Meta:
        db_table = 'ct_leadsig'

