from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Project, Estado, Aggregation, GeoNucleo
from .serializers import ProjectSerializer, MunicipioSerializer
from django.shortcuts import render
from .queries import show_projects_query
from django.db import connection
from django.http import JsonResponse
from .proyectos_ctrl import fn_agregar_nuevos_proyectos
from django.views.decorators.csrf import csrf_exempt
from .models import Municipio
import json



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

def get_municipios(request):
    municipios = Municipio.objects.values('Id_municipio', 'Id_estado', 'clave_municipio', 'nombre_municipio')
    return JsonResponse({'municipios': list(municipios)})
def get_estados(request):
    estados = Estado.objects.values('Id_estado', 'CVE_EST', 'nombre_estado')
    return JsonResponse({'estados': list(estados)})
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
'Cve_Unica'       )
    return JsonResponse({'newProject': list(newProject)})
class MunicipiosPorEstadoView(APIView):
    def get(self, request, Id_estado):
        municipios = Municipio.objects.filter(Id_estado=Id_estado)
        serializer = MunicipioSerializer(municipios, many=True)
        return Response(serializer.data)