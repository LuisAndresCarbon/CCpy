from django.db import models

# Create your models here.
class User(models.Model):
    usuario = models.CharField(max_length=100)
    usuario_email = models.EmailField(unique=True)
    usuario_pw = models.CharField(max_length=100)
    area = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    def __str__(self):
        return self.full_name