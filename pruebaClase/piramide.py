"""piramide"""

h = int(input("Introduce la altura: "))

for i in range (h):
    num_esp = h - i
    num_ast = i + (i+1)
    print(" " * num_esp + "*" * num_ast)
    