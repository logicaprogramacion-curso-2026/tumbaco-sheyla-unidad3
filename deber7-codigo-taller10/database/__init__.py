from database.conexion import DatabaseConnection

# Singleton para la conexión a la base de datos
db = DatabaseConnection()

def get_db():
    """Retorna la instancia de la base de datos"""
    return db