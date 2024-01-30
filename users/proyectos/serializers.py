from rest_framework import serializers
from .models import Project, SigCat

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'

class ProjectSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Project
      
class SigCatSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = SigCat