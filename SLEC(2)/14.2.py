"""Crea una aplicación que dibuje una pirámide invertida de asteriscos usando bucles anidados. Nosotros le pasamos la altura
de la pirámide por teclado."""

altura = int (input("Dime la altura que desea: "))

for i in range (1, altura +1):
   num_esp = i - 1
   print(" " * num_esp, end="")
   num_ast = 2 * (altura - i) +1
   print("*" * num_ast, end="")
   print()
   