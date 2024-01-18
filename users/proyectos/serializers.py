from rest_framework import serializers

from .models import projects

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = '__all__'