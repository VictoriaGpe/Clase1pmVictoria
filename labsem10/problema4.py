import statistics

def calcular_estadisticas(*args):
    if not args:
        return "No se ingresaron números."
    
    numeros = list(args)
    promedio = (lambda nums: sum(nums) / len(nums))(numeros)
    mediana = statistics.median(numeros)
    desviacion_estandar = statistics.stdev(numeros) if len(numeros) > 1 else 0
    
    return {
        "Promedio": promedio,
        "Mediana": mediana,
        "Desviación estándar": desviacion_estandar
    }

# Solicitar entrada del usuario
numeros_usuario = input("Ingrese una lista de números separados por espacios: ")
numeros_lista = list(map(float, numeros_usuario.split()))

# Calcular estadísticas
resultado = calcular_estadisticas(*numeros_lista)

# Mostrar resultados
print("Resultados:")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")
