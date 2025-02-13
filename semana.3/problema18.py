import math

def resolver_ecuacion_cuadratica(a, b, c):
    """Resuelve la ecuación cuadrática ax^2 + bx + c = 0."""
    if a == 0:
        return "No es una ecuación cuadrática."

    # Calcular el discriminante
    discriminante = b**2 - 4*a*c

    # Verificar el tipo de soluciones
    if discriminante > 0:
        # Dos soluciones reales y distintas
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"Dos soluciones reales: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        # Una solución real (raíz doble)
        x = -b / (2 * a)
        return f"Una solución real: x = {x}"
    else:
        # Solucione
