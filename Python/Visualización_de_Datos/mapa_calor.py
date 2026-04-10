import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Trabajo de pandas
df = pd.read_csv('titanic_limpio.csv') # Llamado al csv

numeros = df.select_dtypes(include = ['number']) # Selección de columnas con un condicional dentro del Dataset
correlacion =  numeros.corr() # Se hace una correlación entre columnas seleccionadas

# Trabajo de seaborn

sns.heatmap(correlacion, annot= True, cmap = 'coolwarm') # Creación del mapa de calor
#annot mostrar valores númericos encima del color
#cmap paleta de colores

# Trabajo de matoplotlib
plt.title('Mapa de calor')
plt.show()