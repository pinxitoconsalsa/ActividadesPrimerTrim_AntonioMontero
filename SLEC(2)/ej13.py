"""Crea una aplicación que dibuje una escalera de números, siendo cada línea números
empezando en uno y acabando en el numero de la línea."""

altura = int (input("Dime que altura deseas: "))

for i in range (1, altura + 1):
    for j in range (1, i + 1):
        print(j , end="")
    print()