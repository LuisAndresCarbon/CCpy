from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def show_all(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    # Aquí puedes realizar la lógica de validación del inicio de sesión
    usuario_email = request.data.get('usuario_email', '')
    usuario_pw = request.data.get('usuario_pw', '')

    try:
        user = User.objects.get(usuario_email=usuario_email, usuario_pw=usuario_pw)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
