import monitor
import requests

try:
    monitor.extraccion_datos()
except requests.exceptions.RequestException as error:
    print(f"No hay conexion al API: {error}")