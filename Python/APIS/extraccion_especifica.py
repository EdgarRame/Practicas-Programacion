import requests

try:
    respuesta = requests.get("https://jsonplaceholder.typicode.com/users/2")
    respuesta.raise_for_status()
    datos = respuesta.json()
    print(datos['name'], datos['email'], datos['address']['city'])
except requests.exceptions.RequestException as error:
    print(f"No hay conexion al API: {error}")