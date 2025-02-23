import random

def lanzar_dado():
    return random.randint(1, 6)

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

print("Simulación de lanzamiento:")
print("1. Lanzar un dado")
print("2. Lanzar una moneda")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    print("El dado cayó en:", lanzar_dado())

elif opcion == 2:
    print("La moneda cayó en:", lanzar_moneda())

else:
    print("Opción no válida.")
