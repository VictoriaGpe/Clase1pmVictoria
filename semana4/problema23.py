import numpy as np

def ingresar_matriz(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos de la matriz ({filas}x{columnas}):")
    for i in range(filas):
        fila = list(map(int, input(f"Fila {i+1}: ").split()))
        matriz.append(fila)
    return np.array(matriz)

def mostrar_matriz(nombre, matriz):
    print(f"\n{name}:\n{matriz}")

print("Seleccione una operación con matrices:")
print("1. Suma de matrices")
print("2. Resta de matrices")
print("3. Multiplicación de matrices")
print("4. Transposición de una matriz")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion in [1, 2, 3]:
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    print("\nMatriz A")
    A = ingresar_matriz(filas, columnas)

    print("\nMatriz B")
    B = ingresar_matriz(filas, columnas)

    if opcion == 1:
        resultado = A + B
        operacion = "Suma"
    elif opcion == 2:
        resultado = A - B
        operacion = "Resta"
    elif opcion == 3:
        if A.shape[1] == B.shape[0]:
            resultado = np.dot(A, B)
            operacion = "Multiplicación"
        else:
            print("¡Error! El número de columnas de A debe ser igual al número de filas de B.")
            exit()

    mostrar_matriz(f"Resultado de la {operacion}", resultado)

elif opcion == 4:
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    print("\nMatriz A")
    A = ingresar_matriz(filas, columnas)

    resultado = A.T
    mostrar_matriz("Matriz Transpuesta", resultado)

else:
    print("Opción no válida.")
