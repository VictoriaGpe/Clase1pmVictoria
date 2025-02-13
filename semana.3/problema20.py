# Implementación de Búsqueda Lineal
def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  # Retorna la posición donde se encontró el valor
    return -1  # Retorna -1 si no se encontró el valor

# Implementación de Búsqueda Binaria
def busqueda_binaria(lista, valor):
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor:
            return medio  # Retorna la posición donde se encontró el valor
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1  # Retorna -1 si no se encontró el valor

# Prueba de los algoritmos
lista_prueba = [1, 3, 5, 7, 9, 11, 13, 15]
valor_buscar = 7

# Búsqueda Lineal
resultado_lineal = busqueda_lineal(lista_prueba, valor_buscar)
print(f"Búsqueda lineal: El valor {valor_buscar} {'fue encontrado en la posición ' + str(resultado_lineal) if resultado_lineal != -1 else 'no fue encontrado'}.")

# Búsqueda Binaria
resultado_binario = busqueda_binaria(lista_prueba, valor_buscar)
print(f"Búsqueda 
