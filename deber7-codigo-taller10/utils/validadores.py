def validar_actividad(actividad):
    """Valida que una actividad tenga todos los campos requeridos"""
    required_fields = ['nombre', 'tipo', 'nivel_requerido']
    for field in required_fields:
        if not hasattr(actividad, field):
            return False
    return True

def validar_puntaje(puntaje):
    """Valida que el puntaje esté en el rango 0-100"""
    return 0 <= puntaje <= 100

def formatear_mensaje(mensaje, tipo='info'):
    """Formatea un mensaje con un prefijo según el tipo"""
    prefijos = {
        'info': '[INFO] ',
        'error': '[ERROR] ',
        'exito': '[ÉXITO] ',
        'warning': '[ADVERTENCIA] '
    }
    return f"{prefijos.get(tipo, '[INFO] ')}{mensaje}"