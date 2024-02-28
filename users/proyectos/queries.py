from django.db import connection
from django.http import JsonResponse

def show_projects_query():
    with connection.cursor() as cursor:
        cursor.callproc('getProjectData')
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return JsonResponse({'projects': results})

def insert_project(ProjectName, idaggregation, Counterpart, idnucleoAgrario,idUserCreate):
    with connection.cursor() as cursor:
        cursor.callproc('insert_project', [ProjectName, idaggregation, Counterpart, idnucleoAgrario, idUserCreate])
        result = cursor.fetchone()
    return result

def show_State():
    with connection.cursor() as cursor:
        cursor.callproc('getProjectData')
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return JsonResponse({'projects': results})

def show_Municipality(id_Estado):
    with connection.cursor() as cursor:
        cursor.callproc("MunicipiosByEstado", [id_Estado])
        results = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        if results:
            data = [{'idMunicipio': row[0], 'nameMunicipality': row[1]} for row in results]
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse([], safe=False)

def show_nucleoAgrario(id_mun):
    with connection.cursor() as cursor:
        cursor.callproc("nucleoAgrByMunicipio", [id_mun])
        results = cursor.fetchall()
        if results:
            data = [{'idnucleoAgrario': row[0], 'NameNuc': row[1], 'descripcion': row[2]} for row in results]
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse([], safe=False)