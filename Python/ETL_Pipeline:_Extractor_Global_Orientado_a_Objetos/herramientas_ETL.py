import requests
import datetime

# Obtencion del momento de obtención de los datos
def log_ejecucion(funcion_og):
    def date():
        momento_extraccion = datetime.datetime.now()
        datos_recuperados = funcion_og()
        print(f"Los datos se extrajeron: {momento_extraccion}")
        return datos_recuperados
    return date

# Función para descargar los datos
@log_ejecucion
def extraccion_datos():
    respuesta = requests.get("https://jsonplaceholder.typicode.com/users/")
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos
