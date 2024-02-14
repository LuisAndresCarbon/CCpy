from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Project, Estado, Aggregation, GeoNucleo
from .serializers import ProjectSerializer, MunicipioSerializer
from django.shortcuts import render
from .queries import show_projects_query, insert_project, show_Municipality, show_nucleoAgrario
from django.db import connection
from django.http import JsonResponse
from .proyectos_ctrl import fn_agregar_nuevos_proyectos
from .projectsControl import fn_agregar_nuevos_proyectos
from django.views.decorators.csrf import csrf_exempt
from .models import Municipio
import json
import asyncio


@csrf_exempt
async def agregarProyecto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("👀",data)
            result = await fn_agregar_nuevos_proyectos(data)
            if not isinstance(result, dict):
                result = {'error': 'Error en la lógica'}
            return JsonResponse(result)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def get_municipios(request):
    municipios = Municipio.objects.values('Id_municipio', 'Id_estado', 'clave_municipio', 'nombre_municipio')
    return JsonResponse({'municipios': list(municipios)})

def get_ctagregation(request):
    ag = Aggregation.objects.values('ID_Agregation', 'AgregationID')
    return JsonResponse({'ag': list(ag)})
def get_ctNomNucleo(request):
    geoNucleo = GeoNucleo.objects.values('CVE_GEO', 'NOM_NUC', 'CVE_UNICA')
    return JsonResponse({'geoNucleo': list(geoNucleo)})

@csrf_exempt
def newProject_api_view(request):
    newProject = Project.objects.values('ProjectID',       
'Folio_proyect'   ,
'ProjectName'     ,
'AggregationID'   ,
'CounterpartID'   ,
'Cve_Geo'         ,
'Cve_Est'         ,
'Cve_Mun'         ,
'id_phin',
'Cve_Unica'       ,
'Status')
    return JsonResponse({'newProject': list(newProject)})
class MunicipiosPorEstadoView(APIView):
    def get(self, request, Id_estado):
        municipios = Municipio.objects.filter(Id_estado=Id_estado)
        serializer = MunicipioSerializer(municipios, many=True)
        return Response(serializer.data)

class ShowDetailByphina(APIView):
    def get(self, request, id_phin):
        cursor = connection.cursor()
        cursor.execute("CALL busqueda_CVE_UNICA_Y_TIPO(%s)", [id_phin])
        results = cursor.fetchall()
        data = [{'CVE_UNICA': row[0], 'TIPO': row[1]} for row in results]
        return JsonResponse({'claveUnica': data})








def get_Agrario(request, id_mun):
    results = show_nucleoAgrario(id_mun)
    return results

def get_municipalities(request, id_Estado):
    results = show_Municipality(id_Estado)
    return results
        
def get_estados(request):
    estados = Estado.objects.values('idEstado', 'nomEstado')
    return JsonResponse({'estados': list(estados)})

def get_projects(request):
    if request.method == 'GET':
        data = show_projects_query()
        return data
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
@csrf_exempt
def post_projects(request):
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud JSON
        data = json.loads(request.body)
        
        # Llamar a la función fn_agregar_nuevos_proyectos para insertar el proyecto
        result = fn_agregar_nuevos_proyectos(data)
        
        # Verificar el resultado de la función fn_agregar_nuevos_proyectos
        if result['valido'] == 1:
            return JsonResponse({'message': result['mensaje'], 'idprojects': result['idprojects']})
        else:
            return JsonResponse({'error': result['mensaje_error']})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)