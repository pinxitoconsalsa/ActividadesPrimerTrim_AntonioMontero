
caracter = '4'

filas = 5


espacios_interiores = [1, 3, 6] 

for i in range(filas):
    if i == 0:
       
        print(caracter)
    
    elif i == filas - 1:
        base_caracteres = 9 
        print((caracter + ' ') * 4 + caracter) 
    
    else:
        num_espacios = espacios_interiores[i - 1]
        
        
        print(caracter + (' ' * num_espacios) + caracter)