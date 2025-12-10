"""Escriba un programa que pida la edad por teclado y nos muestra el mensaje de “Eres mayor
de edad”, si y solamente si lo somos."""
edad = 0

while edad < 18:
    try:
        edad = int (input("Introduce tu edad: "))
    
    except ValueError:
        print("Entrada no válida, por favor responda con un número entero.")
        
print("Eres mayor de edad")        
        