"""Escriba un programa que lee dos números y muestra el mayor"""

try:
    num1 = float(input("Introduce num1: "))
    num2 = float(input("Introduce num2: "))
    
    if num1 < num2:
        print(f"{num2} es mayor que {num1}.")
    else:
        print(f"{num1} es mayor que {num2}.")
except ValueError:
    print("Entrada no válida, introduce un número.")