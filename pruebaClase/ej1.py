filas = 11
columnas_max = 6

fila_central = filas // 2


for i in range(filas):

    if i <= fila_central:
        num_estrellas = i + 1
    else:
        num_estrellas = filas - i
    
    
    num_espacios = columnas_max - num_estrellas
    
   
    print(' ' * num_espacios + '*' * num_estrellas)