import requests

try:
    respuesta = requests.get("https://jsonplaceholder.typicode.com/users/")
    respuesta.raise_for_status()
    datos = respuesta.json() # Va fuera del bucle para generar una respuesta JSON
    for i in datos: # Bucle que recorrera el JSON denominado datos
        print(i['name'])
except requests.exceptions.RequestException as error:
    print(f"No hay conexion al API: {error}")