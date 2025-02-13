def contar_vocales_y_consonantes(cadena):
    # Convertir la cadena a minúsculas para uniformidad
    cadena = cadena.lower()
    
    # Inicializar contadores
    vocales = "aeiou"
    contador_vocales = 0
    contador_consonantes = 0

    # Recorrer la cadena y contar vocales y consonantes
    for char in cadena:
        if char.isalpha():  # Verificar si el carácter es una letra
            if char in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1

    return contador_vocales, contador_consonantes

# Ejemplo de uso
cadena = input("Ingresa una cadena: ")
vocales, consonantes = contar_vocales_y_consonantes(cadena)
print(f"Número de vocales: {vocales}")
print(f"Número de consonantes: {consonantes}")
