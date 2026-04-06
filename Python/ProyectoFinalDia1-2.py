# Cabezal
print("*** Analizador de Gastos ***")

# Listas
gastos = []

# Bucle
while True:
    cosas = input("Ingrese nombre de en que salen los gastos o ingrese 'salir' para cerrar: ").lower()
    if cosas == 'salir':
        break

    precios = float(input(f"Ingrese el precio de {cosas}: "))
    gastos.append({"cosas": cosas, "precios": precios})

print("\nReporte de gastos")
