def suma_numeros():
    n = int(input("¿Cuántos números desea sumar?: "))
    suma = 0
    for i in range(n):
        num = float(input(f"Ingrese el número {i+1}: "))
        suma += num
    print("La suma es:", suma)


def producto_numeros():
    n = int(input("¿Cuántos números desea multiplicar?: "))
    producto = 1
    for i in range(n):
        num = float(input(f"Ingrese el número {i+1}: "))
        producto *= num
    print("El producto es:", producto)


def division_dos_numeros():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    if b != 0:
        print("La división es:", a / b)
    else:
        print("Error: No se puede dividir entre cero")


def factorial():
    n = int(input("Ingrese un número entero positivo: "))
    if n < 0:
        print("No se puede calcular el factorial de un número negativo")
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print(f"El factorial de {n} es {fact}")


def tablas_multiplicar():
    n = int(input("Ingrese el número de la tabla (1 al 10): "))
    print(f"Tabla del {n}")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def cuadrado_cubo():
    n = float(input("Ingrese un número: "))
    print("Cuadrado:", n ** 2)
    print("Cubo:", n ** 3)


def promedio_numeros():
    suma = 0
    contador = 0
    while True:
        num = float(input("Ingrese un número (-1 para terminar): "))
        if num == -1:
            break
        suma += num
        contador += 1

    if contador > 0:
        print("El promedio es:", suma / contador)
    else:
        print("No se ingresaron números")


def max_min():
    n = int(input("¿Cuántos números desea ingresar?: "))
    numeros = []

    for i in range(n):
        num = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)

    print("Número máximo:", max(numeros))
    print("Número mínimo:", min(numeros))
    print("Total de números ingresados:", len(numeros))


def menu():
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Suma de n números")
        print("2. Producto de n números")
        print("3. División entre 2 números")
        print("4. Factorial de un número")
        print("5. Tabla de multiplicar")
        print("6. Cuadrado y cubo de un número")
        print("7. Promedio de números")
        print("8. Máximo y mínimo")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            suma_numeros()
        elif opcion == "2":
            producto_numeros()
        elif opcion == "3":
            division_dos_numeros()
        elif opcion == "4":
            factorial()
        elif opcion == "5":
            tablas_multiplicar()
        elif opcion == "6":
            cuadrado_cubo()
        elif opcion == "7":
            promedio_numeros()
        elif opcion == "8":
            max_min()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")


menu()
