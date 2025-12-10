"""Ejercicio 2: Estrella de ocho puntas
Enunciado:

Imprime una estrella de ocho puntas combinando líneas verticales, horizontales y diagonales con asteriscos en una matriz de tamaño impar n x n (ej. 9x9).

Figura para n=9:

*   *   *
 *  *  *
  * * *
*********
  * * *
 *  *  *
*   *   *

  """

h = int (input("introduce la altura que desea: "))

for i in range (h):
    
    linea=""
    
    for j in range(h):
        
        lineaHorizontal= (i==h//2)
        lineaVertical= (j==h//2)
        diagonalIzq = (i==j)
        diagonalDer = (i+j == h-1)        
        
        if lineaVertical or lineaHorizontal or diagonalIzq or diagonalDer:
            linea += "*"
        else:
            linea += " "
    print(linea)
        
  