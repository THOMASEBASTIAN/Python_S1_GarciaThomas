import json

ARCHIVO_JSON = "inmuebles.json"

def guardar_datos(inmuebles):
    with open(ARCHIVO_JSON, 'w') as f:
        json.dump(inmuebles, f, indent=4)

def cargar_datos():
    try:
        with open(ARCHIVO_JSON, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []