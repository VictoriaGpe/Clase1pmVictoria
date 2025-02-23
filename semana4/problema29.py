import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def generar_datos(n=100, media=50, desviacion=15):
    """Genera una muestra aleatoria de datos con distribución normal."""
    return np.random.normal(media, desviacion, n)

def analizar_datos(datos):
    """Calcula y muestra estadísticas básicas."""
    df = pd.DataFrame(datos, columns=["Valores"])
    
    print("\n📊 Estadísticas Descriptivas:")
    print(f"Media: {np.mean(datos):.2f}")
    print(f"Mediana: {np.median(datos):.2f}")
    print(f"Moda: {stats.mode(datos, keepdims=True)[0][0]:.2f}")
    print(f"Desviación estándar: {np.std(datos, ddof=1):.2f}")
    print(f"Varianza: {np.var(datos, ddof=1):.2f}")
    print(f"Rango: {np.ptp(datos):.2f}")
    print(f"Percentil 25: {np.percentile(datos, 25):.2f}")
    print(f"Percentil 75: {np.percentile(datos, 75):.2f}")

def graficar_datos(datos):
    """Genera histogramas y gráficos de distribución."""
    plt.figure(figsize=(12, 5))
    
    # Histograma
    plt.subplot(1, 2, 1)
    plt.hist(datos, bins=15, color="skyblue", edgecolor="black", alpha=0.7)
    plt.title("Histograma de Datos")
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    
    # Gráfico de distribución con Seaborn
    plt.subplot(1, 2, 2)
    sns.kdeplot(datos, color="red", fill=True, alpha=0.4)
    plt.title("Distribución de Datos")
    plt.xlabel("Valores")
    
    plt.show()

def main():
    print("\n📌 Generador y Analizador de Datos Estadísticos")
    n = int(input("Ingrese el número de datos a generar: "))
    media = float(input("Ingrese la media esperada: "))
    desviacion = float(input("Ingrese la desviación estándar: "))

    datos = generar_datos(n, media, desviacion)
    
    analizar_datos(datos)
    graficar_datos(datos)

if __name__ == "__main__":
    main()
