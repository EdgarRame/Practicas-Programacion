# Obtención del Subtotal
cuenta = float(input("Introduzca el subtotal de la cuenta: "))
print (f"El subtotal es: {cuenta:.2f}") #  Este es lo que sale en la cuenta
print("Introduzca una cantidad valida.")

# IVA
iva = cuenta * 0.16 # Cuanto es el IVA
print (f"El iva de la cuenta es: {iva:.2f}")