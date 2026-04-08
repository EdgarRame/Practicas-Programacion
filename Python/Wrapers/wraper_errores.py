def detector_errores(funcion_og):
    def error():
            try:
                funcion_og()
            except ValueError:
                print("La función fallo pero el sistema sigue en pie")
            return error
    return error

@detector_errores
def fallo():
    numero = int(input("Introduce un número: "))
    print(numero)

fallo()