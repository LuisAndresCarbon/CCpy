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
        
def fnprojecthist(ProjectName, idaggregation, Counterpart, idnucleoAgrario,idUserCreate):
    with connection.cursor() as cursor:
        cursor.callproc('insert_project', [ProjectName, idaggregation, Counterpart, idnucleoAgrario, idUserCreate])
        result = cursor.fetchone()
    return result

def fnprojehistdetail(project_id):
    try:
        with connection.cursor() as cursor:
            cursor.callproc("projecthistdetails", [project_id])
            results = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]

            data = []
            for row in results:
                data.append(dict(zip(column_names, row)))

        return JsonResponse(data, safe=False)
    except Exception as e:
        # Manejar cualquier error aquí
        print("Error:", e)
        return JsonResponse([], safe=False)

def fnspprojecthistory(idprojects, ProjectName, idaggregation, Counterpart, idnucleoAgrario,Justification, iduserrequest):
    with connection.cursor() as cursor:
        cursor.callproc('spprojecthistory', [idprojects, ProjectName, idaggregation, Counterpart, idnucleoAgrario, Justification, iduserrequest])
        result = cursor.fetchone()
    return result

def FnNostifyProjecthist():
    with connection.cursor() as cursor:
        cursor.callproc('NotifyProyectoHist')
        result = cursor.fetchall()
        column_names = [column[0] for column in cursor.description]
        return [dict(zip(column_names, row)) for row in result]