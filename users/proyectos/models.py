# proyectos/models.py

from django.db import models
from .queries import show_projects_query
from django.db import connection
class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=255)
    AggregationID = models.IntegerField()
    CounterpartID = models.IntegerField()
    Cve_Geo = models.IntegerField()
    Cve_Est = models.IntegerField()
    Cve_Mun = models.IntegerField()
    Cve_Unica = models.IntegerField()
    Status = models.CharField(max_length=255)
    DateCreate = models.DateTimeField()
    IDUserCreate = models.IntegerField()
    DateModify = models.DateTimeField()
    IDUserModify = models.IntegerField()
def show_projects(cls):
        with connection.cursor() as cursor:
            cursor.execute(show_projects_query())
            projects = cursor.fetchall()
        return projects