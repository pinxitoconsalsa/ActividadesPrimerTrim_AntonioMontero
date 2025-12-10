"""piramide inv"""

h = int(input("introduce la altura que desea: "))

for i in range (h):
    num_esp = i
    num_ast = 2 * (h-i) - 1
    print(" " * num_esp + "*" * num_ast)