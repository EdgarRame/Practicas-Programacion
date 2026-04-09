import pandas as pd

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

    def imprimir_csv(self):
        limpio = pd.read_csv('datos_limpios.csv')
        print(limpio)