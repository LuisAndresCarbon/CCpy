from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from ..user_api.serializers import UserSerializer
from django.http import JsonResponse
from ..user_api.models import Usuario  # Asegúrate de tener un archivo models.py en users/



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # users/views.py

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    data = [{'nombre': usuario.nombre} for usuario in usuarios]
    return JsonResponse({'usuarios': data})

    