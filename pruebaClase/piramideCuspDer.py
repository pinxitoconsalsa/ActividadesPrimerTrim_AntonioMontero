h = int(input("Introduce la altura que deseas: "))
n = h//2 +1
for i in range(1, n+1):
    num_ast = i
    print("*" * num_ast)
for i in range(n-1, 0, -1):
    num_ast = i
    print("*" * num_ast)