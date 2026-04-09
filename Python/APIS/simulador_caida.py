import requests

try:
    respuesta = requests.get("https://jsonplaceholder.typicode.com/usuarios_falsos/")
    respuesta.raise_for_status()
    datos = respuesta.json()
    print(datos)
except requests.exceptions.RequestException as error:
    print(f"No hay conexion al API: {error}")