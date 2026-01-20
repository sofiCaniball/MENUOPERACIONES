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



