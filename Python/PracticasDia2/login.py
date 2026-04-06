# Cabezal
print("*** Login ***")

# Variables
password_maestra = "Contraseña"

while True:
    intento = str(input("Introduzca su contraseña: "))
    if intento == password_maestra:
        break
    else:
        print("Contraseña incorrecta")
        print("Vuelva a ingresar la contraseña")