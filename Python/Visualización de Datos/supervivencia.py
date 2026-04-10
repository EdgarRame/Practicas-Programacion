import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic_limpio.csv')

# 1. Configurar el estilo
sns.set_theme(style="whitegrid")

# 2. Crear un gráfico de barras
sns.countplot(x='Sex', hue = 'Survived', data=df,
            palette='viridis')
plt.yticks([0, 10, 20, 30, 40, 50, 60,
            70, 80, 90])

# Personalizar grafica
plt.title('Distribución de Supervivencia (0 = No, 1 = Si)')
plt.xlabel('Género')
plt.ylabel('Cantidad de pasajeros')

# Mostrar grafica
plt.show()