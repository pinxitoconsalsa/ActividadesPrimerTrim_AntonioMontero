"""Tablero 17X17"""

for i in range (1, 17+ 1):
    for j in range (1, 17 +1):
        if (i) % 2 == 0:   
            print("*", end=" ")
        else:
            print(" ", end="")
    print()    
    