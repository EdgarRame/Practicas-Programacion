class Vehiculo: # Para generar mi clase
# Creación de objetos
    def __init__(self, marca, modelo, combustible): # __init__ es el constructor con sus atributos
        self.marca = marca # self es para referirse asi mismo como un get y set
        self.modelo = modelo
        self.combustible = combustible

# Creación del metodos (Que hara el objeto)
    def encender(self):
        print(f"Has encendido el vehiculo {self.modelo} de la marca {self.marca} pero necesita {self.combustible}")

# Creacion de los objetos (instanciar objetos en una clase)
vehiculo_1 = Vehiculo("Nissan", "March", "gasolina")
vehiculo_2 = Vehiculo("Tesla", "Tesla Model 3", "electricidad")
vehiculo_3 = Vehiculo("Toyota", "Mirai", "hidrogeno")

# Llamado a ejecutar los metodos de los objetos
vehiculo_1.encender()
vehiculo_2.encender()
vehiculo_3.encender()