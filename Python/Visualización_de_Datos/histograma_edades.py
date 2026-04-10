import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic_limpio.csv')

# 1. Configurar el estilo
sns.set_theme(style="whitegrid")

# 2. Crear histograma
plt.hist(df['Age'], bins = 30, color = 'orange', edgecolor =  'black')

# Personalizar
plt.title('Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show() # Importante: sin esto no se abre la ventana del gráfico