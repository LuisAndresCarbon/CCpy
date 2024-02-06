from rest_framework import serializers
from .models import Project, Municipio

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'

class ProjectSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Project
      
class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['Id_municipio', 'Id_estado', 'clave_municipio', 'nombre_municipio']