from .SpProjectArea import SetprojectArea

def fnSetnewProjectArea(datos):
    try:
        # Llamar al procedimiento almacenado para insertar el proyecto
        result = SetprojectArea(datos ['IdProject'],
                                datos ['Idcertificacion'],
                                datos ['SuperficieTotalPhina'],
                                datos ['Achurado'],
                                datos ['Expopriado'],
                                datos ['LinkPHINA'],
                                datos ['SuperficieTotal'],
                                datos ['IdsolicitudRAN'],
                                datos ['SuperficiePlanoInterno'],
                                datos ['AreasExpropiadas'],
                                datos ['AñodelPlan'],
                                datos ['LinkPlanoInterno'],
                                datos ['IdStatusValidacionAP'],
                                datos ['ObservacionesAP'],
                                datos ['LinkAP'],
                                datos ['IdLeadSIG'])
        if result:
            # Verificar si el primer conjunto de resultados contiene la cadena 'valido'
            if len(result) > 0 and result[0] == 'valido':
                # Verificar si el segundo conjunto de resultados contiene un ID de área de proyecto
                if len(result) >= 1:
                    idareadeproyecto = result[1] if result[1] else None
                    return {'valido': True, 'idareadeproyecto': idareadeproyecto}
                else:
                    raise Exception('No se recibió el ID del área del proyecto')
            else:
                # Si la respuesta es '1', indicando que el proyecto ya tiene un área
                if len(result) > 0 and result[0] == 1:
                    raise Exception('El proyecto ya tiene un área')
                else:
                    raise Exception('Respuesta no reconocida del procedimiento almacenado')
        else:
            raise Exception('No se recibieron resultados del procedimiento almacenado')

    except Exception as e:
        print(f"Error al agregar proyectos: {e}")
        return {'valido': False, 'mensaje_error': str(e)}