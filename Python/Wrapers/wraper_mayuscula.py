def mayuscula(funcionog):
    def interecepta():
        texto = input("Ingrese un texto: ")
        resultado = funcionog(texto)
        print(f"El texto es: {resultado}")
        return interecepta
    return interecepta

#Creación de wraper
@mayuscula
def conversion(texto):
    return texto.upper()

conversion()