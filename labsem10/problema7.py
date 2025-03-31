import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivote]
    medio = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)

def busqueda_binaria(arr, objetivo):
    inicio, fin = 0, len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Generar lista aleatoria
tamano_lista = int(input("Ingrese el tamaño de la lista: "))
lista = [random.randint(1, 100) for _ in range(tamano_lista)]
print("Lista original:", lista)

# Ordenar la lista
lista_ordenada = quicksort(lista)
print("Lista ordenada:", lista_ordenada)

# Búsqueda en la lista
numero_buscar = int(input("Ingrese un número a buscar en la lista: "))
resultado = busqueda_binaria(lista_ordenada, numero_buscar)
if resultado != -1:
    print(f"El número {numero_buscar} se encuentra en la posición {resultado}.")
else:
    print(f"El número {numero_buscar} no está en la lista.")
