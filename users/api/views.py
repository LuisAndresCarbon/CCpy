from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def prueba(request):
    
    return Response("hola feo")
    