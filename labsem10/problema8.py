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

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    medio = len(arr) // 2
    izquierda = mergesort(arr[:medio])
    derecha = mergesort(arr[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Generar lista ingresada por el usuario
tamano_lista = int(input("Ingrese el tamaño de la lista: "))
lista = [int(input(f"Ingrese el número {i+1}: ")) for i in range(tamano_lista)]
print("Lista original:", lista)

# Ordenar la lista con Mergesort
lista_ordenada = mergesort(lista)
print("Lista ordenada con Mergesort:", lista_ordenada)

# Búsqueda en la lista
numero_buscar = int(input("Ingrese un número a buscar en la lista: "))
resultado = busqueda_binaria(lista_ordenada, numero_buscar)
if resultado != -1:
    print(f"El número {numero_buscar} se encuentra en la posición {resultado}.")
else:
    print(f"El número {numero_buscar} no está en la lista.")
