import pandas as pd


# Pedir el Dataset y guardarlo en una variable
csv = ('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# Diccionario con los datos a trabajar

# Funcion de leer el archivo csv guardado en su variable
df = pd.read_csv(csv)


# Operaciones en Pandas
print(df.head(10))

print(df.tail(10))   # Muestra las 10 ultimas filas

print(df.describe())

print(df.info()) #Muestra nombres de todas las columnas y el tipo de datos de cada columna