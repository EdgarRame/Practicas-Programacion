import requests
import datetime

def log_ejecucion(funcion_og):
    def date():
        momento_extraxion = datetime.datetime.now()
        funcion_og()
        print(f"Los datos se extrajeron: {momento_extraxion}")
        return date
    return date

@log_ejecucion
def extraccion_datos():
    respuesta = requests.get("https://jsonplaceholder.typicode.com/users/1")
    respuesta.raise_for_status()
    datos = respuesta.json()
    print(datos)