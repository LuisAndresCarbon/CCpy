from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([JWTAuthentication])  # Aquí se aplica el decorador
@permission_classes([IsAuthenticated])
def show_all(request):
    try:
     users = User.objects.all()
     serializer = UserSerializer(users, many=True)
     return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)

@api_view(['POST'])
def login(request):
    # lógica de validación del inicio de sesión
    usuario_email = request.data.get('usuario_email', '')
    usuario_pw = request.data.get('usuario_pw', '')

    try:
        user = User.objects.get(usuario_email=usuario_email, usuario_pw=usuario_pw)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
