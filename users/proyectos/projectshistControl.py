from .queries import fnspprojecthistory
def fnSolicitarUpdateproyectoshist(datos, user_id):
    try:
        # Verificar si los datos están vacíos
        if not datos['idprojects']or not datos['ProjectName'] or not datos['idaggregation'] or not datos['Counterpart'] or not datos['idnucleoAgrario']or not datos['Justification']:
            raise Exception('Los datos son requeridos')
        print("datos:",datos)
        # Llamar al procedimiento almacenado para insertar el proyecto
        result = fnspprojecthistory(            
            datos['idprojects'],                
            datos['ProjectName'],
            datos['idaggregation'],
            datos['Counterpart'],
            datos['idnucleoAgrario'],
            datos['Justification'],
            user_id
        )

        if result[0] == 'INSERT':
            # Obtener el ID del idproyectohist insertado
            idproyectohist = result[1]
            return {
                'idproyectohist': idproyectohist
            }
        else:
            # Obtener el ID del idproyectohist actualizado
            idproyectohist = datos['idprojects']
            return {
                'idproyectohist': idproyectohist
            }
    except Exception as e:
        if str(e) == 'Los datos son requeridos':
            raise Exception('Los datos son requeridos')
        else:
            raise Exception('Error al guardar el proyecto')