"""Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado."""

altura = int (input("introduce la altura que desees: "))
for i in range(1, altura + 1):
    num_espacios = altura - i
    print(" " * num_espacios, end="")
    
    num_ast = 2 * i - 1
    print("*" * num_ast)
        
        
       