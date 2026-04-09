class Empleado():
    
# Constructor
    def __init__(self, id, nombre, email, empresa):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.empresa = empresa

# Metodo del constructor
    def mostrar_ficha(self):
        print(self.id, self.nombre, self.email, self.empresa)