def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

num = int(input("Ingrese un número: "))
print(f"El factorial de {num} es: {factorial_recursivo(num)}")
