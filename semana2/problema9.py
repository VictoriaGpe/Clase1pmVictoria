def generar_pares_impares(limite):
    pares = [num for num in range(0, limite + 1, 2)]
    impares = [num for num in range(1, limite + 1, 2)]
    return pares, impares

limite = int(input("Ingrese el límite: "))

pares, impares = generar_pares_impares(limite)

print(f"Números pares hasta {limite}: {pares}")
print(f"Números impares hasta {limite}: {impares}")
