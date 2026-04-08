import atencion as at

propina = int(input("¿Cuánta propina quiere entregar 10, 20, 30 o 0: "))
def obtener_propina(propina):
    try:
        cuenta = at.cuenta
        iva = at.iva
        if propina == 10:
            total = print(f"El total es: {at.cuenta + (at.cuenta * 0.10)+ at.iva:.2f}")
        elif propina == 20:
            total = print(f"El total es: {at.cuenta + (at.cuenta * 0.20) + at.iva:.2f}")
        elif propina == 30:
            total = print(f"El total es: {at.cuenta + (at.cuenta * 0.30) + at.iva:.2f}")
        elif propina == 0:
            total = print (f"El Total de la cuenta es: {at.cuenta + at.iva:.2f}")
    except ValueError:
        print("Introduzca un porcentaje valido.")   
obtener_propina(propina)