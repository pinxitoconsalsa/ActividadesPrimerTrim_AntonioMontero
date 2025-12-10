"""Leer una cadena desde teclado y mostrarla carácter por carácter usando un ciclo for y el índice."""

cadena = input("Ingrese una cadena de texto: ")

longitud = len(cadena)

for i in range (longitud):
    caracter = cadena[i]
    print(f"Indice {i + 1}: {caracter}")
    
