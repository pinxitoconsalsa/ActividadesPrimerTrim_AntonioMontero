"""Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado."""

altura = int (input("Ingresa altura: "))

for i in range (1, altura + 1):
    espacios = i - 1
    print(" " * espacios, end="")
    
    ast = 2 * (altura - i) + 1
    print("*" * ast)
print()
