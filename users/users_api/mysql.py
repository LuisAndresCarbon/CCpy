import mysql.connector

# Configuración de conexión a la base de datos
config = {
    'user': 'root',
    'password': 'Unico123',
    'host': 'localhost',  # Puedes cambiar esto según tu configuración
    'database': 'db-portafolio',
    'raise_on_warnings': True,
}

# Intentar establecer la conexión
try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Conexión establecida con éxito a MySQL Server version {db_info}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar la conexión al finalizar
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Conexión cerrada.")
        print(connection.queries)