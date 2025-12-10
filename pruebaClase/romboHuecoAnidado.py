"""Crea un diamante hueco usando dos bucles anidados."""

altura = 9
for i in range (altura):
    
    linea=""
    
    for j in range (altura):
          
          diagonal_sup_izq = (j == (altura // 2) - i) and (i<=(altura//2))
          diagonal_sup_der = (j == (altura // 2) + i) and (i<=(altura//2))
          diagonal_inf_izq = (i == (altura // 2) + j) and (i> (altura//2))
          diagonal_inf_der = (j == (altura - 1) - i + (altura // 2))  and (i> (altura//2))  
          if diagonal_sup_izq or diagonal_sup_der or diagonal_inf_izq or diagonal_inf_der:
              linea +="*"
          else:
              linea +=" "
    print(linea)          