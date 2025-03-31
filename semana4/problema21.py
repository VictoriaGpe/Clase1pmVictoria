import math

def area_circulo(radio):
    return math.pi * radio**2

def area_cuadrado(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def volumen_esfera(radio):
    return (4/3) * math.pi * radio**3

def volumen_cubo(lado):
    return lado ** 3

def volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura

print("Elija una opción:")
print("1. Área de un círculo")
print("2. Área de un cuadrado")
print("3. Área de un rectángulo")
print("4. Área de un triángulo")
print("5. Volumen de una esfera")
print("6. Volumen de un cubo")
print("7. Volumen de un cilindro")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    radio = float(input("Ingrese el radio del círculo: "))
    print("El área del círculo es:", area_circulo(radio))

elif opcion == 2:
    lado = float(input("Ingrese el lado del cuadrado: "))
    print("El área del cuadrado es:", area_cuadrado(lado))

elif opcion == 3:
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    print("El área del rectángulo es:", area_rectangulo(base, altura))

elif opcion == 4:
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    print("El área del triángulo es:", area_triangulo(base, altura))

elif opcion == 5:
    radio = float(input("Ingrese el radio de la esfera: "))
    print("El volumen de la esfera es:", volumen_esfera(radio))

elif opcion == 6:
    lado = float(input("Ingrese el lado del cubo: "))
    print("El volumen del cubo es:", volumen_cubo(lado))

elif opcion == 7:
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    print("El volumen del cilindro es:", volumen_cilindro(radio, altura))

else:
    print("Opción no válida.")
