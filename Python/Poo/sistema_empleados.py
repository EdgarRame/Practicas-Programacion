class Empleado:
    def __init__(self, nombre, puesto, salario_base):
        self.nombre = nombre
        self.puesto = puesto
        self.salario_base = salario_base

    def calcular_salario_neto(self):
        impuesto = self.salario_base * 0.16
        return self.salario_base - impuesto


empleados = []

for i in range(3):
    print(f"\nEmpleado {i + 1}")
    nombre = input("Ingrese el nombre del empleado: ")
    puesto = input("Ingrese el puesto: ")
    salario_base = float(input("Ingrese el salario base: "))

    empleado = Empleado(nombre, puesto, salario_base)
    empleados.append(empleado)

print("\nResumen de salarios netos:")
for empleado in empleados:
    salario_neto = empleado.calcular_salario_neto()
    print(f"{empleado.nombre}: {salario_neto:.2f}")