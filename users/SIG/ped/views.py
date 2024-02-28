from .models import resultpedAP, seccionAA, poblacionAA,ActivityAG,clasEncuestas,subSidiosAA,clasPendienteAA,ChangeofCoverage,resultPedAA
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def fnCatresultpedAP(request):
    resultpedap = resultpedAP.objects.values('IdResultadoPEDAP', 'ResultadoPEDAP')
    return JsonResponse({'resultpedap': list(resultpedap)})

def fnCatseccionAA(request):
    seccionaa = seccionAA.objects.values('IdSeccionPEDAA', 'SeccionPEDAA')
    return JsonResponse({'seccionaa': list(seccionaa)})

def fnCatpoblacionAA(request):
    poblacionaa = poblacionAA.objects.values('IdPoblacionAA', 'PoblacionAA')
    return JsonResponse({'poblacionaa': list(poblacionaa)})

def fnCatActivityAG(request):
    activityAg = ActivityAG.objects.values('IdActividadAgropecuaria', 'ActividadAgropecuaria')
    return JsonResponse({'activityAg': list(activityAg)})

def fnCatEncuestas(request):
    escuestas = clasEncuestas.objects.values('IdEncuestas', 'Encuentas')
    return JsonResponse({'escuestas': list(escuestas)})

def fnCatsubSidiosAA(request):
    subsidioaa = subSidiosAA.objects.values('IdSubsidiosAA', 'SubsidiosAA')
    return JsonResponse({'subsidioaa': list(subsidioaa)})

def fnCatPendienteAA(request):
    pendienteaa = clasPendienteAA.objects.values('IdPendienteAA', 'PendienteAA')
    return JsonResponse({'pendienteaa': list(pendienteaa)})

def fnCatChangeofCoverage(request):
    cambiocoberturaaa = ChangeofCoverage.objects.values('IdCambioCoberturaAA', 'CambioCoberturaAA')
    return JsonResponse({'cambiocoberturaaa': list(cambiocoberturaaa)})

def fnresultPedAA(request):
    resultadopedaa = resultPedAA.objects.values('IdResultadoPEDAA', 'ResultadoPEDAA')
    return JsonResponse({'resultadopedaa': list(resultadopedaa)})
