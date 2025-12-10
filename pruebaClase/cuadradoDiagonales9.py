"""Imprime un cuadrado de lado n con borde y diagonales en asteriscos, y un cuadro hueco centrado dentro.
Figura para n=9:"""

n = 9

for i in range (n):
     
    linea = ""
    
    for j in range (n):
        
        bordes_cuadrado = (j == 0) or (j == n-1) or (i ==0) or (i == n-1)
        
        diagonal_sup_izq = (j == i + 1) and (i <= (n //2) -1 )
        
        diagonal_sup_der = (j == n - i - 2) and (i <= (n//2 - 1))
        
        diagonal_inf_izq = (i == j + 1) and (i > (n //2) )
        
        diagonal_inf_der = (i == n - j ) and (i > n // 2)
        
        if bordes_cuadrado or diagonal_sup_izq or diagonal_sup_der or diagonal_inf_izq or diagonal_inf_der:
            linea+= "*"
        else:
            linea += " "
    print(linea)