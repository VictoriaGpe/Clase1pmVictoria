def suma_n_naturales(n):
    return (n * (n + 1)) // 2  # Fórmula de la suma de los primeros N números naturales

def suma_serie_aritmetica(a, d, n):
    return (n / 2) * (2 * a + (n - 1) * d)  # Fórmula de la suma de una serie aritmética

def suma_serie_geometrica(a, r, n):
    if r == 1:
        return a * n  # Caso especial cuando la razón es 1
    return a * (1 - r**n) / (1 - r)  # Fórmula de la suma de una serie geométrica

print("Seleccione el tipo de serie numérica para calcular la suma:")
print("1. Suma de los primeros N números naturales")
print("2. Suma de una serie aritmética")
print("3. Suma de una serie geométrica")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    n = int(input("Ingrese el valor de N: "))
    print(f"La suma de los primeros {n} números naturales es:", suma_n_naturales(n))

elif opcion == 2:
    a = float(input("Ingrese el primer término (a): "))
    d = float(input("Ingrese la diferencia común (d): "))
    n = int(input("Ingrese el número de términos (n): "))
    print(f"La suma de la serie aritmética es:", suma_serie_aritmetica(a, d, n))

elif opcion == 3:
    a = float(input("Ingrese el primer término (a): "))
    r = float(input("Ingrese la razón (r): "))
    n = int(input("Ingrese el número de términos (n): "))
    print(f"La suma de la serie geométrica es:", suma_serie_geometrica(a, r, n))

else:
    print("Opción no válida.")
