"""Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero)"""

try:
    num1 = float (input("Indique el valor de num1: "))
    num2 = float (input("Indique el valor de num2: "))

    suma = num1+num2
    resta = num1-num2
    prod = num1*num2
    

    if num2 == 0:
        div = "No se puede realizar"
        
    else:
        div = num1/num2
        
    print(f"{suma}, {resta}, {prod}, {div}")    
       
except ValueError:
    print("Entrada no válida")