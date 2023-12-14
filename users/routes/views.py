# rutas/views.py
from django.http import JsonResponse
from controladores.con_mysql import conectar_base_de_datos, cerrar_conexion
from models.usuario import Usuario

def lista_usuarios(request):
    connection = conectar_base_de_datos()
    
    if connection:
        try:
            usuarios = Usuario.objects.all()
            data = [{'nombre': usuario.nombre} for usuario in usuarios]
            return JsonResponse({'usuarios': data})

        except Exception as e:
            return JsonResponse({'error': str(e)})

        finally:
            cerrar_conexion(connection)
    else:
        return JsonResponse({'error': 'No se pudo conectar a la base de datos.'})
