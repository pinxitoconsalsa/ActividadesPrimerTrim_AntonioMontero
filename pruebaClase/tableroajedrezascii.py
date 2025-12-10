"""Tablero 17X17"""
altura = 13
for i in range (altura):
    linea = ""
    for j in range (altura):
        contorno = (i==0) or (i==altura) or (j == 0) or (j == altura-1)
        
        
        if contorno:
            linea += "*"
        else:
            linea += " "        
    print(linea)    
    