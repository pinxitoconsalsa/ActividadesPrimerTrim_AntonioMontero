"""Piramide dividida en 4 partes iguales, con una altura introducida por teclado
    


"""

h = int (input("Introduce la altura que desee: "))


for i in range (h):
    linea = ""
    for j in range (h):

        lado_izq_ext = ((j*2) + i == h - 1)
        lado_der_ext = ((j*2) - i == h - 1)
        horizontal_gra = (i == h-1) and (j%2 == 0)
        horizontal_peq = (i == h//4) and ((h//2) - 1 <= j <= (h//2) + 1)
        diagonal_izq = (i>= h//2) and (j * 2 == i)
        diagonal_der = (i >= h/2) and ((h - 1 - j) * 2 == i)

        if lado_izq_ext or lado_der_ext or horizontal_gra or diagonal_izq or horizontal_peq or diagonal_der :
            linea += "*"
        else:
            linea += " "
    print(linea)




