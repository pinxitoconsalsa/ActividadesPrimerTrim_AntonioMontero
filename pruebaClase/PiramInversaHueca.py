"""Piramide inversa hueca"""

h = int (input("Introduce la altura que desee: "))

for i in range (h):
    num_esp = i
    num_esp_int = 2 * (h-i) - 3
    if i == h-1:
        print(" " * num_esp + "*")
    elif i==0:
        print((num_esp_int + 2) * "*")
    else: 
        print(" " * num_esp + "*" + " " * num_esp_int + "*")