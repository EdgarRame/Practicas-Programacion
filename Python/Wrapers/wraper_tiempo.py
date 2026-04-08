import time as time

def medir_tiempo(funcion_og):
    def bucle():
        inicio = time.time()
        funcion_og()
        fin = time.time()
        tiempo = fin - inicio
        print(f"El recorrido demoro: {tiempo:.6f}segundos")
        return bucle
    return bucle

@medir_tiempo
def recorrido():
    contador = 0
    for i in range(1_000_000):
        contador += 1

recorrido()