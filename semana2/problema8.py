import math

def calcular_area(radio):
    return math.pi * radio ** 2

def calcular_circunferencia(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area(radio)
circunferencia = calcular_circunferencia(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"La circunferencia del círculo es: {circunferencia:.2f}")
