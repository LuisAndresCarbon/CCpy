from django.db import connection
from django.http import JsonResponse

def SetprojectArea(IdProject,
        Idcertificacion,
        SuperficieTotalPhina,
        Achurado,
        Expopriado,
        LinkPHINA,
        SuperficieTotal,
        IdsolicitudRAN,
        SuperficiePlanoInterno,
        AreasExpropiadas,
        AñodelPlan,
        LinkPlanoInterno,
        IdStatusValidacionAP,
        ObservacionesAP,
        LinkAP,
        IdLeadSIG):
        with connection.cursor() as cursor:
            cursor.callproc('insertProjectarea', [IdProject,
        Idcertificacion,
        SuperficieTotalPhina,
        Achurado,
        Expopriado,
        LinkPHINA,
        SuperficieTotal,
        IdsolicitudRAN,
        SuperficiePlanoInterno,
        AreasExpropiadas,
        AñodelPlan,
        LinkPlanoInterno,
        IdStatusValidacionAP,
        ObservacionesAP,
        LinkAP,
        IdLeadSIG])
            result = cursor.fetchone()
            print("SetprojectArea",result[0])
            return result