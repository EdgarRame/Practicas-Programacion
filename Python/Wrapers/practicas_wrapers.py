def bienvenida(funcion_og):
    def envoltorio():
        print("Hola usuario!!")
        funcion_og()
        return envoltorio
    return envoltorio

@bienvenida
def clima():
    print("El clima es muy caluroso")

@bienvenida
def despedida():
    print("Adios Usuairo")

clima()
despedida()