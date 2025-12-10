"""Diibuja el contorno de una pirámide"""

h = int (input("Introduce la altura que desee: "))

for i in range (h):
    num_esp = h - (i+1)
    num_esp_int = i + (i - 1)
    if i == h-1:
        print("*" * (h + i))
    elif i == 0:
        print(" " * num_esp + "*")
        
    else:
        print(" " * num_esp + "*" + " " * num_esp_int + "*")