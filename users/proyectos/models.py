from django.db import models

# Create your models here. CONSISTENCIA DE DATOS


class projects(models.Model):
    ProjectName = models.CharField(max_length=200, null=False, blank=False)
    AggregationID = models.CharField(max_length=100, null=False, blank=False)
    CounterpartID = models
    Cve_Geo = models.TextField()
    Cve_Est = models.IntegerField()

    def __str__(self):
        return self.full_name
    
