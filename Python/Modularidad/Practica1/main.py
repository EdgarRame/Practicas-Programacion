import herramientas_texto as ht
import calculos as promedio

# Ingreso de textos
texto_1 = input("Ingres el primer texto: ")
texto_2 = input("Ingrese el segundo texto: ")
texto_3 = input("Ingrese el tecer texto: ")

# Mostras textos
texto_original = print(f"Los textos son: {texto_1}, {texto_2} y {texto_3}")

# Uso de funciones
texto_1_proces = ht.mayusculas_texto(ht.limpiar_espacios(texto_1))
texto_2_proces = ht.mayusculas_texto(ht.limpiar_espacios(texto_2))
texto_3_proces = ht.mayusculas_texto(ht.limpiar_espacios(texto_3))

# Impresion de textos procesados
print(f"Los textos procesados son: {texto_1_proces}{texto_2_proces}{texto_3_proces}")

# Ingreso de numeros
numero = []

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numero_3 = int(input("Ingrese el tercer número: "))

numero.extend([numero_1, numero_2, numero_3])

# Uso de funciones
calculo = promedio.calcular_promedio(numero)

# Mostrar lista

print(f"Los numeros son: {int(numero_1)}, {int(numero_2)} y {int(numero_3)}")
print(f"El promedio es: {int(calculo)}")