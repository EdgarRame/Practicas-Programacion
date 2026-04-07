class Banco:

    print("*** Aplicación de banco ***")

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def depositar(self):
        try:
            monto = float(input("¿Cuánto va a depositar: "))
            self.saldo += monto
            print(f"Su saldo actual es de: {self.saldo:.2f}")
        except ValueError:
            print("Ingrese una cantidad valida.")

    def retirar(self):
        try:
            monto = float(input(f"Ingrese la cantidad de dinero que va a retirar:"))
            if monto > self.saldo:
                print("Saldo insuficiente.")
            else:
                self.saldo -= monto
                print(f"Su saldo actual es de: {self.saldo:.2f}")
        except ValueError:
                print("Ingrese una cantidad valida.")
    
    def menu(self):
        while True:
            accion = input("Bienvenido al banco, ¿qué acción realizará ('retirar', 'depositar' o 'salir')?: ").lower()
            try:
                if accion == 'depositar':
                    self.depositar()
                elif accion == 'retirar':
                    self.retirar()
                elif accion == 'salir':
                    print("Saliendo....")
                    break
            except ValueError:
                print("Introduzca una opción valida.")

cuenta = Banco("Edgar", 500.00)

cuenta.menu()