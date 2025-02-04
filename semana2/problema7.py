def analizar_numero(num, multiplo_de=None):
    if num % 2 == 0:
        tipo = "par"
    else:
        tipo = "impar"
    
    if multiplo_de is not None:
        if num % multiplo_de == 0:
            multiplo = f"es múltiplo de {multiplo_de}"
        else:
            multiplo = f"no es múltiplo de {multiplo_de}"
    else:
        multiplo = ""

    return f"El número {num} es {tipo}. {multiplo}"

# Ejemplo de uso
num = int(input("Ingrese un número: "))
multiplo_de = input("Ingrese un número para verificar si es múltiplo (o presione Enter para omitir): ")

if multiplo_de:
    multiplo_de = int(multiplo_de)
    print(analizar_numero(num, multiplo_de))
else:
    print(analizar_numero(num))
