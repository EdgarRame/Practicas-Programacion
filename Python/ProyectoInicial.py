# Cabezal
print("*** Gestión de alumnos***")

# Lista
alumno = []

# Bucle While
while True:
    nombre = input("Introduzca el nombre del alumno(o ingrese 'salir' para terminar): ").lower()
    if nombre == 'salir':
        break
    
    edad = int(input(f"Introduzca la edad de {nombre}: "))
    alumno.append({"nombre": nombre, "edad": edad})


# Reporte de alumnos
print("\n Reporte de los alumnos")
print(len(alumno))

# Edades
menor = min(alumno, key=lambda x: x['edad'])
print(f"El alumno más joven es: {menor['nombre']}, y su edad es: {menor['edad']}")