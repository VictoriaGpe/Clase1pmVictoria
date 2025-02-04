def fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Ejemplo de uso
num_terminos = int(input("Ingrese el número de términos: "))
print(fibonacci(num_terminos))
