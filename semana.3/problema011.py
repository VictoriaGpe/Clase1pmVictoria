def es_palindromo(cadena):
    # Eliminar espacios y convertir la cadena a minúsculas
    cadena = ''.join(c for c in cadena if c.isalnum()).lower()
    
    # Verificar si es un palíndromo
    return cadena == cadena[::-1]

# Ejemplo de uso
cadena = input("Ingresa una cadena para verificar si es palíndromo: ")
if es_palindromo(cadena):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
