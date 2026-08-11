import json
import re
import os

def cargar_json(ruta):
    """Carga un archivo JSON y retorna su contenido"""
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def guardar_json(ruta, datos):
    """Guarda datos en un archivo JSON"""
    try:
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False

def limpiar_texto(texto):
    """Limpia un texto eliminando caracteres especiales y espacios extra"""
    if not texto:
        return ""
    # Eliminar caracteres especiales
    texto = re.sub(r'[^\w\sáéíóúñÑ]', '', texto)
    # Eliminar espacios múltiples
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()
