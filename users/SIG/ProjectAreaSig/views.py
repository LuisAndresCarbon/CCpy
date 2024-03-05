from .models import Areaproject, CatalogRequestalRan, Catalogcertificacion, Catalogstatusvalidacionap, Catalogleadsig
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .CtrlprojectArea import fnSetnewProjectArea

# Create your views here.
def getAreaproject(request):
    areaproject = Areaproject.objects.values('idareadeproyecto','IdProject','Idcertificacion','SuperficieTotalPhina','Achurado','Expopriado','LinkPHINA','SuperficieTotal','IdsolicitudRAN','SuperficiePlanoInterno'  ,'AreasExpropiadas'  ,'AñodelPlan','LinkPlanoInterno','IdStatusValidacionAP','ObservacionesAP','LinkAP','IdLeadSIG')
    return JsonResponse({'areaproject': list(areaproject)})
def getCatRan(request):
    catRan = CatalogRequestalRan.objects.values('IdsolicitudRAN', 'SolictiudalRAM')
    return JsonResponse({'catRan': list(catRan)})
def fnctCertificacion(request):
    catCer = Catalogcertificacion.objects.values('Idcertificacion', 'Certificacion')
    return JsonResponse({'catCer': list(catCer)})
def fngetctstatusvalidnap(request):
    catValidnap = Catalogstatusvalidacionap.objects.values('IdStatusValidacionAP', 'StatusValicionAP')
    return JsonResponse({'catValidnap': list(catValidnap)})

def fngetCatalogleadsig(request):
    leadSIG = Catalogleadsig.objects.values('IdLeadSIG', 'LeadSIG')
    return JsonResponse({'leadsig': list(leadSIG)})


@csrf_exempt
def fnprojectsAreas(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    try:
        data = json.loads(request.body)
        # Llamar a la función fnSetnewProjectArea para insertar el proyecto
        result = fnSetnewProjectArea(data)

        # Verificar el resultado de la función fnSetnewProjectArea
        if result['valido']:
            return JsonResponse({'message': 'Se guardó correctamente', 'idareadeproyecto': result['idareadeproyecto']})
        else:
            return JsonResponse({'error': result['mensaje_error']}, status=400)
    
    except Exception as e:
        print(f"Error en fnprojectsAreas: {e}")
        return JsonResponse({'error': 'Error interno del servidor'}, status=500)