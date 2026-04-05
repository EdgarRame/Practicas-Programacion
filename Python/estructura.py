# Listas
lenguajes = ["Python", "Java", "C++", "SQL"]
lenguajes.append("NoSQL") # Agregar elemento

# Bucle e iteración
print("Lenguajes en mi curso:")
for index, lenguaje in enumerate(lenguajes):
    print(f"{index + 1}. {lenguaje}")

# Condicional
if "Python" in lenguajes:
    print("Python es el lenguaje actual.")