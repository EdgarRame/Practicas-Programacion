from funciones_pandas import AnalizadorPro

ruta = ('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

analizador = AnalizadorPro(ruta)

analizador.datos_nulos()
analizador.filtrar_nulos()
analizador.guardar_csv()
analizador.imprimir_csv()
