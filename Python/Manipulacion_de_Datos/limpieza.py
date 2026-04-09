import pandas as pd

csv = ('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

df = pd.read_csv(csv)

# Identificación de valores nulos
print(df.isnull().sum()) # Muestra cuantos valores nulos hay en cada columna

# Rellenar datos
df['Age'] = df['Age'].fillna(df['Age'].median())

# Borrado de filas con más de tres columnas nulas
df = df.dropna(thresh = len(df.columns) - 3)

# Borrado de columna unica de datos con null
df = df.dropna()

# Creación del archivo titanic_limpio para la impresión
df.to_csv('titanic_limpio.csv', index = False)

print("************************************")

# Guardar el archivo en una variable para su impreción
df_limpio = pd.read_csv('titanic_limpio.csv')

print(df_limpio)

# Comprobación final de datos nulos
print(df.isnull().sum())