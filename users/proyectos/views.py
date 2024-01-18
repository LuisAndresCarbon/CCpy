from .queries import show_projects_query
from django.db import connection
from .models import Project
from .serializers import projectSerializer
from django.http import JsonResponse


def show_projects(request):
    with connection.cursor() as cursor:
        cursor.execute(show_projects_query())
        projects = cursor.fetchall()

    # Si tus resultados son tuplas, ajusta la lógica según sea necesario
        with connection.cursor() as cursor:
            cursor.execute(show_projects_query())
        # Obtener los resultados como instancias del modelo Project
            projects = [Project(*row) for row in cursor.fetchall()]
    # Serializar los resultados usando un serializador Django REST Framework
    serializer = projectSerializer(projects, many=True)
    serialized_projects = serializer.data

    # Devolver la respuesta en formato JSON
    return JsonResponse({'projects': serialized_projects}, safe=False)