"""Imprime la letra M mayúscula usando asteriscos en una matriz cuadrada de tamaño impar n.
Las líneas de la M deben visualizarse usando asteriscos, con espacios en el resto."""

h = int (input ("Introduce la altura que desee: "))

if h % 2 == 0 or h <=3:
    print("entrada inválida, pon un numero impar mayor o igual que 3.")

for i in range (h):

    linea = ""

    for j in range (h):
        laterales= (j==0) or (j==h-1)
        diagonal_izq = (i == j) and (i <= h//2 )
        diagonal_der = (j == h - (i+1)) and (i <= h//2 )

        if laterales or diagonal_izq or diagonal_der:
            linea += "*"
        else:
            linea += " "
    print(linea)

