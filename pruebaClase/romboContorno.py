"""Dibuja el contorno de un rombo"""

while True:
    try:
        altura = int(input("Introduce la altura que desee (debe ser impar y positiva): "))
        if altura < 0 or altura % 2 == 0:
            print("La altura debe ser impar y positiva")
        else:
            break
    except ValueError:
        print("La entrada es inválida")
        
n = altura + 1 // 2

for i in range (1, n + 1):
    num_esp = n - i
    num_esp_int = 2 * i - 3
    if num_esp_int < 0:
        print(" " * num_esp + "*")
    else:
        print(" " * num_esp + "*" + " " * num_esp_int + "*")

for i in range (n-1, 0, -1):
    num_esp = n - i
    num_esp_int = 2 * i - 3
    if num_esp_int < 0:
        print(" " * num_esp + "*")
    else:
        print(" " * num_esp + "*" + " " * num_esp_int + "*")
    
    