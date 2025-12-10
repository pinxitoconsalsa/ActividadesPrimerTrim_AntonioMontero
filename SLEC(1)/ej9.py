"""Dibuja un ordinograma de un programa que pida la edad por teclado y nos muestra el
mensaje de “Eres mayor de edad” o el mensaje de “Eres menor de edad."""


try:      
    
    edad = int (input("Introduce tu edad: "))   
      
    if edad < 18:           
         print("Eres menor de edad.")
    else:
             print("Eres mayor de edad.") 
                     
except ValueError:
    print("Entrada no válida, debe responder con un úmero entero.")
    edad = 0
    