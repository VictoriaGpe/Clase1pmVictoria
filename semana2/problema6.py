def interes_compuesto(capital, tasa, tiempo):
    monto = capital * (1 + tasa / 100) ** tiempo
    return monto

# Ejemplo de uso
capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés anual (%): "))
tiempo = int(input("Ingrese el tiempo en años: "))

monto_final = interes_compuesto(capital, tasa, tiempo)
interes_ganado = monto_final - capital

print(f"El monto final después de {tiempo} años es: {monto_final:.2f}")
print(f"El interés ganado es: {interes_ganado:.2f}")
