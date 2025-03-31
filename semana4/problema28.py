class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"✅ Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("❌ La cantidad debe ser mayor a 0.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("❌ Fondos insuficientes.")
        elif cantidad <= 0:
            print("❌ La cantidad debe ser mayor a 0.")
        else:
            self.saldo -= cantidad
            print(f"✅ Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")

    def consultar_saldo(self):
        print(f"💰 Saldo actual: ${self.saldo:.2f}")

def menu():
    cuenta = CuentaBancaria(1000)  # Saldo inicial de $1000

    while True:
        print("\n🏦 Simulador de Cuenta Bancaria")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cuenta.consultar_saldo()

        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)

        elif opcion == "3":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)

        elif opcion == "4":
            print("👋 Saliendo del banco. ¡Gracias por usar nuestro servicio!")
            break

        else:
            print("❌ Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
