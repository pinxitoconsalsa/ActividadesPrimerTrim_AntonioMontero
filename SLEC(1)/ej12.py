"""Escriba un programa que lea un número y dice si es positivo o negativo, consideramos el
cero como positivo."""

try:
    num = int (input("Dime un número: "))
    
    if num < 0:
        print("El número es negativo.")
    elif num > 0:
        print("El número es positivo.")
    else:
        print("El `0´ no es positivo ni negativo; se considera un número neutro. Es el punto medio entre los números positivos y negativos, y en la aritmética estándar, no tiene signo. ")
except ValueError:
    print("Entrada no válido tolay.")