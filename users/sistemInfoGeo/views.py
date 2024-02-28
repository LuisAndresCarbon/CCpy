from django.shortcuts import render
from .models import Areaproject, CatalogRequestalRan, Catalogcertificacion, Catalogstatusvalidacionap, Catalogleadsig
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
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
    catValidnap = Catalogstatusvalidacionap.objects.values('IdstatusValidacionAP', 'StatusValicionAP')
    return JsonResponse({'catValidnap': list(catValidnap)})

def fngetCatalogleadsig(request):
    leadSIG = Catalogleadsig.objects.values('IdLeadSIG', 'LeadSIG')
    return JsonResponse({'leadsig': list(leadSIG)})

