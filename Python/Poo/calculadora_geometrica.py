class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        print(f"El área del rectangulo es: {self.base * self.altura}")

    def calcular_perimetro(self):
        print(f"El perimetro del rectangulo es: {(2 * self.base) + (2 * self.altura)}")

base = int(input("Introduzca la base del rectangulo: "))
altura = int(input("Intruduzca la altura del rectangulo: "))

rectangulito = Rectangulo(base, altura)

rectangulito.calcular_area()
rectangulito.calcular_perimetro()