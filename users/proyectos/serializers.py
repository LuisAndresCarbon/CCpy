from rest_framework import serializers
from .models import Project, Municipio

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'
