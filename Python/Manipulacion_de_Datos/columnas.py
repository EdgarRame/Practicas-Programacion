import pandas as pd

# Llamado al csv
csv = pd.read_csv('titanic_limpio.csv')


# Creación de columna Familiares y sume la columna SibSP y Parch
csv["Familiares"] = csv['SibSp'] + csv['Parch']


# Creación de columna es adulto con condición
csv["Es_Adulto"] = csv['Age'] > 18

csv.to_csv('titanic_modificado.csv', index = False)

df_columnas = pd.read_csv('titanic_modificado.csv')

print(df_columnas)