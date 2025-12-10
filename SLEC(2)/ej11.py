"""Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de
la escalera por teclado."""

altura = int (input("Dime la altura que desea: "))
for i in range (1, altura + 1):
    print("*" * i)
