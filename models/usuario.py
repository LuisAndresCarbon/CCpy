# modelos/usuario.py
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
