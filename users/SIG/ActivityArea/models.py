from django.db import models

# Create your models here.
class clasVersionaa(models.Model):
    IdversionAA = models.TextField(primary_key=True)
    VersionAA = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_versionaa'

class clasStatusv(models.Model):
    IdStatusValidacionAA = models.TextField(primary_key=True)
    StatusValidacionAA = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'ct_statusvalidacionaa'