"""Genera un triangulo sin relleno con la cuspide a la izquierda"""
n = 7

altura = 2*n - 1

for i in range (1, n+1):
    num_esp_ext = n - i
    num_esp_int = i - 2
    if num_esp_int < 0:
        print(" " * num_esp_ext + "*" )
    else:
        print(" " * num_esp_ext + "*" + " " * (num_esp_int ) + "*")

for i in range (n-1, 0, -1):
    num_esp_ext = n - i
    num_esp_int = i - 2
    if num_esp_int < 0:
        print(" " * num_esp_ext + "*" )
    else:
        print(" " * num_esp_ext + "*" + " " * (num_esp_int) + "*")