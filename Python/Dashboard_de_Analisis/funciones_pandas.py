import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AnalizadorPro:

    def __init__(self, ruta_csv):
        self.df = pd.read_csv(ruta_csv)

    def datos_nulos(self):
        porcentaje = (self.df.isnull().sum()/len(self.df)) * 100
        print(porcentaje)

    def filtrar_nulos(self):
        self.df['Age'] = self.df['Age'].fillna(self.df['Age'].median())
        self.df = self.df.dropna(thresh = len(self.df.columns) - 3)
        self.df = self.df.dropna()

    def guardar_csv(self):
        self.df.to_csv('datos_limpios.csv', index = False)

class VisualizacionPro:

    def __init__(self, limpio):
        self.limpio = pd.read_csv(limpio)

    def reporte_supervivencia(self):
        try:
            # Creación de la grafica
            sns.countplot(x='Sex', hue = 'Survived', data= self.limpio,
                palette='viridis')
            plt.yticks([0, 10, 20, 30, 40, 50, 60,
                        70, 80, 90])

            # Personalizar grafica
            plt.title('Distribución de Supervivencia (0 = No, 1 = Si)')
            plt.xlabel('Género')
            plt.ylabel('Cantidad de pasajeros')
            
            #Guardar grafica como archivo png
            plt.savefig('img/supervivencia.png', dpi=300, bbox_inches='tight')
        except KeyError as error:
            print(f"Error faltan columnas necesarias: {error}")

    def reporte_edades(self):
        try:
            plt.clf()
            plt.hist(self.limpio['Age'], bins = 30, color = 'orange', edgecolor =  'black')
            # Personalizar
            plt.title('Edades')
            plt.xlabel('Edad')
            plt.ylabel('Frecuencia')

            #Guardar grafica como archivo png
            plt.savefig('img/edades.png', dpi=300, bbox_inches='tight')
        except KeyError as error:
            print(f"Error faltan columnas necesarias: {error}")

    def analisis_tarifas(self):
        try:
            plt.clf()
            #Crear correlación de dos columnas
            graf =  self.limpio[['Age', 'Fare']]
            relacion= graf.corr()
            #Crear scatterplot
            sns.regplot(x = 'Age', y = 'Fare', data = self.limpio,
                        scatter_kws={'alpha': 0.5, 'color': 'blue'})
            # PErsonalizar scatterplot
            plt.title('Analisis de tarifas')
            plt.xlabel('Edad')
            plt.ylabel('Tarifa')
            #Guardar como png
            plt.savefig('img/tarifas.png', dpi=300, bbox_inches='tight')
            #Mostrar
            plt.show()
        except KeyError as error:
            print(f"Columnas necesarias no existen: {'error'}")
