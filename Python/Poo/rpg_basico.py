class Personaje:
    def __init__(self, nombre, raza, nivel, hp):
        self.nombre = nombre
        self.raza = raza
        self.nivel = nivel
        self.hp = hp

# Metodo para ver el estado
    def estado(self):
        print(f"Las estadisticas de {self.nombre} son: raza: {self.raza}, nivel: {self.nivel} y vida {self.hp}")

# Metodo para subir de nivel
    def subir_nivel(self):
        self.nivel += 1
        self.hp += 20
        print (f"Has subido al nivel: {self.nivel}, tu hp ha subido y ahora es: {self.hp}")

# Metodo para recibir daño
    def recibir_daño(self):
        self.hp -= 7
        if self.hp <= 0:
            print("Has sido derrotado")
        else:
            print("Has recibido 7 de daño!!")

# Función de menu
def menu():
    while True:
        try:
            accion = input("Bienvenido a juego RPG primero creemos tu personaje (escribe 'crear') o prefieres salir (escribe 'salir'): ").lower()
            if accion == 'crear':
                try:
                    nombre = input("¿Cómo se llamare el personaje?: ")
                    raza = input("¿Qué raza es tu peronsaje?: ")
                    vida = int(input("¿Cuanta vida tendra tu personaje: "))
                    aventurero = Personaje(nombre, raza, 1, vida)
                    print(f"Tu personaje es: \n")
                    aventurero.estado()
                    while True:
                        try:
                            juego = input("¿Quieres 'entrenar', 'pelear', ver el 'estado' o 'salir'?: ").lower()
                            if juego == 'entrenar':
                                aventurero.subir_nivel()
                            elif juego == 'pelear':
                                aventurero.recibir_daño()
                            elif juego == 'estado':
                                aventurero.estado()
                            elif juego == 'salir':
                                print("Saliendo al menu...")
                                break
                            else:
                                print("Introduzca unicamente 'entrenar', 'pelear' o 'salir': ")
                        except ValueError:
                            print("Introduzca valores validos.")
                except ValueError:
                    print("Escribe unicamente con caracteres del abecedario")
            elif accion == 'salir':
                break
        except ValueError:
            print("Introduzca un valor valido.")
menu()