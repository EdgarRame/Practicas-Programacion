# Cabezal
print("Calculadora de propinas")

# Inputs y prints
cuenta = float(input("Introduzca el subtotal de la cuenta: "))
print (f"El subtotal es: {cuenta:.2f}") #  Este es lo que sale en la cuenta

iva = cuenta * 0.16 # Cuanto es el IVA
print (f"El iva de la cuenta es: {iva:.2f}")

propina = int(input("¿Cuánta propina quiere entregar 10, 20, 30 o 0: "))
def obtener_propina(propina):
    if propina == 10:
        print(f"El total es: {cuenta + (cuenta * 0.10)+ iva:.2f}")
    elif propina == 20:
        print(f"El total es: {cuenta + (cuenta * 0.20) + iva:.2f}")
    elif propina == 30:
        print(f"El total es: {cuenta + (cuenta * 0.30) + iva:.2f}")
    elif propina == 0:
        print (f"El Total de la cuenta sin propina es: {cuenta + iva:.2f}")
obtener_propina(propina)