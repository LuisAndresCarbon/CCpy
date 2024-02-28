from django.db import models

# Create your models here.
class resultpedAP(models.Model):
    IdResultadoPEDAP = models.TextField(primary_key=True)
    ResultadoPEDAP = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_resultadopedap'

class seccionAA(models.Model):
    IdSeccionPEDAA = models.TextField(primary_key=True)
    SeccionPEDAA = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_seccionpedaa'

class poblacionAA(models.Model):
    IdPoblacionAA = models.TextField(primary_key=True)
    PoblacionAA = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_poblacionaa'

class ActivityAG(models.Model):
    IdActividadAgropecuaria = models.TextField(primary_key=True)
    ActividadAgropecuaria = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_actividadagropecuaria'

class clasEncuestas(models.Model):
    IdEncuestas = models.TextField(primary_key=True)
    Encuentas = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_encuestas'

class subSidiosAA(models.Model):
    IdSubsidiosAA = models.TextField(primary_key=True)
    SubsidiosAA = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_subsidiosaa'

class clasPendienteAA(models.Model):
    IdPendienteAA = models.TextField(primary_key=True)
    PendienteAA = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_pendienteaa'


class ChangeofCoverage(models.Model):
    IdCambioCoberturaAA = models.TextField(primary_key=True)
    CambioCoberturaAA = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_cambiocoberturaaa'

class resultPedAA(models.Model):
    IdResultadoPEDAA = models.TextField(primary_key=True)
    ResultadoPEDAA = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_resultadopedaa'




