#Inputs y Prints
nombre = input("Ingrese su nombre completo: ")
print(nombre)

#Contar caracteres
longitud = len(nombre.replace(" ", "")) # Eliminar espacios para contar solo caracteres
print("El número de caracteres en tu nombre es: ", longitud) # Aquí se cuentan los caracteres