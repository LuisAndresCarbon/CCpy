from django.db import connection
from django.http import JsonResponse

def setsolicitudRAN():
    with connection.cursor() as cursor:
        cursor.callproc('ctsolicitudAlRan')
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return JsonResponse({'solicitudalran': results})