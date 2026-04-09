import pandas as pd

# Opciones para mostrar el dataframe completo
#pd.set_option('display.max_rows', None)

# Llamado al csv
csv = pd.read_csv('titanic_limpio.csv')

# Filtrando para mostrar unicamente los de primera clase y los que sobrevivieron
filtrado = csv[(csv['Pclass'] == 1) & (csv['Survived'] == 1)]

# Ordenado de mayor a menor en las tarifas de los boletos
filtrado.sort_values(by = 'Fare', ascending = False, inplace = True)

# Contar cuantos hombre sobrevivieron
hombres = len(filtrado[(filtrado['Sex'] == 'male')])
mujeres = len(filtrado[(filtrado['Sex']== 'female')])



# Impreción del filtrado inicial
print(filtrado)

# Impresión de los hombre y mujeres que sobrevivieron
print(f"Los hombres que sobrevivieron fueron: {hombres}")
print(f"Las mujeres que sobrevivieron fueron: {mujeres}")