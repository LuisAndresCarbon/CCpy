from .models import Estado, aggregation
from .queries import show_projects_query,show_Municipality,show_nucleoAgrario
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .projectsControl import fn_agregar_nuevos_proyectos


def get_Agrario(request, id_mun):
    results = show_nucleoAgrario(id_mun)
    return results

def get_municipalities(request, id_Estado):
    results = show_Municipality(id_Estado)
    return results
        
def get_estados(request):
    estados = Estado.objects.values('idEstado', 'nomEstado')
    return JsonResponse({'estados': list(estados)})

def getaggregation(request):
    agregado = aggregation.objects.values('idaggregation', 'descripcion')
    return JsonResponse({'aggregation': list(agregado)})

def get_projects(request):
    if request.method == 'GET':
        data = show_projects_query()
        return data
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
@csrf_exempt
def post_projects(request):
    if request.method == 'POST':
        # Obtener el ID del usuario autenticado
        user_id = request.user.id
        # Obtener los datos del cuerpo de la solicitud JSON
        data = json.loads(request.body)
        data['idUserCreate'] = user_id
        # Llamar a la función fn_agregar_nuevos_proyectos para insertar el proyecto
        # Pasando el ID del usuario autenticado como argumento
        result = fn_agregar_nuevos_proyectos(data, user_id)
        # Verificar el resultado de la función fn_agregar_nuevos_proyectos
        if result['valido'] == 1:
            return JsonResponse({'message': result['mensaje'], 'idprojects': result['idprojects']})
        else:
            return JsonResponse({'error': result['mensaje_error']})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)