"""Piramide izq hueca"""
h = int (input("Introduce la altura que desee: "))

n = h //2 + 1

for i in range (0, n+1):
    num_esp= n - i
    num_esp_int = i
    if i > 0:
        print(" " * num_esp + "*" + " " * num_esp_int + "*")
    else:
        print(" " * num_esp + "*")
for i in range (n, 0, -1):
    num_esp= n - i
    num_esp_int = i 
    if i > 0:
        print(" " * num_esp + "*" + " " * num_esp_int + "*")
    else:
        print(" " * num_esp + "*")
    print(" " * num_esp + "*" + " " * num_esp_int + "*")