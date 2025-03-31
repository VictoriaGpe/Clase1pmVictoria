def convertir_longitud(valor, unidad_origen, unidad_destino):
    factores = {
        "m": 1, "km": 1000, "mi": 1609.34, "ft": 0.3048, "in": 0.0254
    }
    return valor * (factores[unidad_origen] / factores[unidad_destino])

def convertir_peso(valor, unidad_origen, unidad_destino):
    factores = {
        "g": 1, "kg": 1000, "lb": 453.592, "oz": 28.3495
    }
    return valor * (factores[unidad_origen] / factores[unidad_destino])

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "C" and unidad_destino == "F":
        return (valor * 9/5) + 32
    elif unidad_origen == "C" and unidad_destino == "K":
        return valor + 273.15
    elif unidad_origen == "F" and unidad_destino == "C":
        return (valor - 32) * 5/9
    elif unidad_origen == "F" and unidad_destino == "K":
        return (valor - 32) * 5/9 + 273.15
    elif unidad_origen == "K" and unidad_destino == "C":
        return valor - 273.15
    elif unidad_origen == "K" and unidad_destino == "F":
        return (valor - 273.15) * 9/5 + 32
    else:
        return valor  # Si las unidades son iguales

def menu():
    while True:
        print("\n🌍 Conversor de Unidades")
        print("1. Longitud (m, km, mi, ft, in)")
        print("2. Masa/Peso (g, kg, lb, oz)")
        print("3. Temperatura (C, F, K)")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            valor = float(input("Ingrese el valor: "))
            unidad_origen = input("Unidad de origen (m, km, mi, ft, in): ").strip()
            unidad_destino = input("Unidad destino (m, km, mi, ft, in): ").strip()
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
            print(f"{valor} {unidad_origen} equivale a {resultado:.4f} {unidad_destino}")

        elif opcion == "2":
            valor = float(input("Ingrese el valor: "))
            unidad_origen = input("Unidad de origen (g, kg, lb, oz): ").strip()
            unidad_destino = input("Unidad destino (g, kg, lb, oz): ").strip()
            resultado = convertir_peso(valor, unidad_origen, unidad_destino)
            print(f"{valor} {unidad_origen} equivale a {resultado:.4f} {unidad_destino}")

        elif opcion == "3":
            valor = float(input("Ingrese el valor: "))
            unidad_origen = input("Unidad de origen (C, F, K): ").strip()
            unidad_destino = input("Unidad destino (C, F, K): ").strip()
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
            print(f"{valor}°{unidad_origen} equivale a {resultado:.2f}°{unidad_destino}")

        elif opcion == "4":
            print("Saliendo del conversor...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
