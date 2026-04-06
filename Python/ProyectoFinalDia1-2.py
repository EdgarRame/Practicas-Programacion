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

if len(gastos) > 0:
    total = sum(g['precios'] for g in gastos)
    mas_caro = max(gastos, key = lambda g: g['precios'])
    mas_barato = min(gastos, key = lambda g: g['precios'])
    if total < 10000.00:
        print("Los gastos son: ")
        contador = 0
        for i, elemento in enumerate (gastos, start=1):
                print(f"{i}. {elemento['cosas']}")
        print(f"Los costos totales son: {total:.2f}")
        print(f"El gasto más caro fue {mas_caro['cosas']} con el precio de: (${mas_caro['precios']:.2f})")
        print(f"El gasto más barato fue {mas_barato['cosas']} con el precio de: (${mas_barato['precios']:.2f})")
    else:
        print("Presupuesto excedido.")
else:
    print("No se añadireon gastos: ")