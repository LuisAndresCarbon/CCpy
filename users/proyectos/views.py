from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Project, SigCat
from .serializers import ProjectSerializer
from django.shortcuts import render
from .queries import show_projects_query
from django.db import connection
from django.http import JsonResponse
from .proyectos_ctrl import fn_agregar_nuevos_proyectos
from django.views.decorators.csrf import csrf_exempt

import json

@api_view (['GET','POST'])

def newProject_api_view(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute(show_projects_query())
            # Obtener los resultados como instancias del modelo Project
            projects = [Project(*row) for row in cursor.fetchall()]
        
        # Serializar los resultados usando un serializador Django REST Framework
        serializer = ProjectSerializer(projects, many=True)
        serialized_projects = serializer.data

        # Devolver la respuesta en formato JSON
        return JsonResponse({'projects': serialized_projects}, safe=False)

    



def show_all_municipal(request):
    # Llamamos al método de clase show_all_projects en el modelo SigCat
    catalogo = SigCat.show_all_municipal()
    context = {'catalogo': catalogo}
    return JsonResponse(context, safe=False)



@csrf_exempt
async def agregarProyecto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("👀",data)
            result = await fn_agregar_nuevos_proyectos(data)
            print(f"Resultado de la función externa: {result}")
            if not isinstance(result, dict):
                result = {'error': 'Error en la lógica'}
            return JsonResponse(result)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)