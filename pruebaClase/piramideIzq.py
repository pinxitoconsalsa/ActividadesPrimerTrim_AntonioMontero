"""Piramide con cúspide a la izq"""

h = int (input("Introduce la altura que desee: "))

n = h  // 2 +1

for i in range (1, n+1):
   
    num_esp = n-i
    num_ast= i
    
    print(" " * num_esp + "*" * num_ast)
    
for i in range (n-1, 0, -1):
    
    num_esp = n-i
    num_ast= i
    
    print(" " * num_esp + "*" * num_ast)