def calculadora():
    print("Calculadora Simple")
    print("Operaciones disponibles: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Elige una opción (1/2/3/4): ")
    
    if opcion in ('1', '2', '3', '4'):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == '1':
            print(f"El resultado de la suma es: {num1 + num2}")
        elif opcion == '2':
            print(f"El resultado de la resta es: {num1 - num2}")
        elif opcion == '3':
            print(f"El resultado de la multiplicación es: {num1 * num2}")
        elif opcion == '4':
            if num2 != 0:
                print(f"El resultado de la división es: {num1 / num2}")
            else:
                print("Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    calculadora()
