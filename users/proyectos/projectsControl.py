from .queries import insert_project

def fn_agregar_nuevos_proyectos(datos, user_id):
    try:
        # Llamar al procedimiento almacenado para insertar el proyecto
        result = insert_project(datos['ProjectName'], datos['idaggregation'], datos['Counterpart'], datos['idnucleoAgrario'], user_id)
        print("optenido", datos)
        if result[0] == 'valido':
            return {
                'valido': 1,
                'mensaje': 'Se guardó correctamente',
                'idprojects': result[1]
            }
        else:
            raise Exception('The Project Name already exists')
    except Exception as e:
        print(f"Error al agregar proyectos: {e}")
        return {
            'valido': 0,
            'mensaje_error': str(e)
        }