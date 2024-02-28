from .models import clasVersionaa, clasStatusv
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


def fncatversionaa(request):
    versionaa = clasVersionaa.objects.values('IdversionAA', 'VersionAA')
    return JsonResponse({'versionaa': list(versionaa)})

def fnStatusValidacion(request):
    statusvalidacion = clasStatusv.objects.values('IdStatusValidacionAA', 'StatusValidacionAA')
    return JsonResponse({'statusvalidacion': list(statusvalidacion)})
