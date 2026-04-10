import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Llamado al Dataset
df = pd.read_csv('titanic_limpio.csv')

# Configuración del estilo
sns.set_theme(style = 'darkgrid')

plt.figure(figsize = (8,5))
sns.barplot(x = 'Pclass', y = 'Fare', data = df, palette = 'Oranges',
            hue = 'Pclass',legend = False)

# Etiquetas de la grafica
plt.title('Comparativa de Clases')
plt.xlabel('Clases: (1 = Primera Clase 2 = Confort 3 = Economica)')
plt.ylabel('Precios (Precios que se pagan)')

# Se muestra la grafica
plt.show()
