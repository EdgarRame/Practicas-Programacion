import herramientas_ETL as htl
import modelo_datos as poo
import requests


#Creación de lista
base_de_datos = []

# Manejo de errores
try:
    datos_crudos = htl.extraccion_datos()

# Se mape el API para con el for obtener los datos requeridos
    for usuarios in datos_crudos:
        id_emp = usuarios['id']
        nombre_emp = usuarios['name']
        email_emp = usuarios['email']
        empresa_emp = usuarios['company']['name']

        # Creación de objetos
        empleado = poo.Empleado(id_emp, nombre_emp, email_emp, empresa_emp)

        # Se guardan en la lista los datos
        base_de_datos.append(empleado)

        #Llamado al metodo
        empleado.mostrar_ficha()
except requests.exceptions.RequestException as error:
    print(f"Error de conexión al API: {error}")