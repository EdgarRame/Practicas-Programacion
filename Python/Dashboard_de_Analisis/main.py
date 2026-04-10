from funciones_pandas import *

ruta = ('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
limpio = ('datos_limpios.csv')


analizador = AnalizadorPro(ruta)

analizador.datos_nulos()
analizador.filtrar_nulos()
analizador.guardar_csv()

visualizador = VisualizacionPro(limpio)

visualizador.reporte_supervivencia()
visualizador.reporte_edades()
visualizador.analisis_tarifas()