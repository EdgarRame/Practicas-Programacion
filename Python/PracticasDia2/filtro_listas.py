# Cabezal
print("*** Filtro de Listas***")

# Lista
numeros = [65, 44, 90, 22, 59, 27, 75, 17, 96, 18]
limite = 50

# Filtrar los números mayores a 50
mayores = [i for i in numeros if i >  limite]
# Impresión de la lista y de los números mayores a 50 de la lista
print(numeros)
print(mayores)