from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self) -> str:
        return self.nombre