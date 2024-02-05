from rest_framework import serializers
from .models import Project

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'

class ProjectSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Project
      
