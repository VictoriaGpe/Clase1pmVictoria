def analizar_texto(texto):
    # Convertir el texto a minúsculas y eliminar signos de puntuación
    import string
    texto = texto.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Número total de palabras
    total_palabras = len(palabras)
    
    # Conjunto de palabras únicas
    palabras_unicas = set(palabras)
    total_unicas = len(palabras_unicas)
    
    # Frecuencia de cada palabra
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    # Encontrar la palabra más frecuente
    palabra_mas_frecuente = max(frecuencia, key=frecuencia.get)
    frecuencia_maxima = frecuencia[palabra_mas_frecuente]
    
    # Mostrar el resumen
    print("Resumen del análisis del texto:")
    print(f"Número total de palabras: {total_palabras}")
    print(f"Cantidad de palabras únicas: {total_unicas}")
    print("Frecuencia de cada palabra:")
    for palabra, cantidad in frecuencia.items():
        print(f"  {palabra}: {cantidad}")
    print(f"Palabra más frecuente: '{palabra_mas_frecuente}' (Aparece {frecuencia_maxima} veces)")

# Solicitar al usuario que ingrese un texto
texto_usuario = input("Ingrese un texto para analizar: ")
analizar_texto(texto_usuario)
