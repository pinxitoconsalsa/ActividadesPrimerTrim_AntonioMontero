"""Ejercicio 1: Diamante hueco
Enunciado:

Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.

Figura para n=5:

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
    
"""

altura = int (input("introduce la altura que desee: "))
if altura %2 == 0 or altura <=1:
    print("Tiene que ser impar y mayor que 1")

n = (altura + 1)//2

for i in range (1, n+1):
    num_esp = n - i
    num_esp_int = 2 * (i-1) - 1
    if i !=1:
        print(" " * num_esp + "*" + " " * num_esp_int + "*")
    else:
        print(" " * num_esp + "*")

for i in range (n-1, 0, -1):
     num_esp = n - i
     num_esp_int = 2 * (i-1) - 1
     if i !=1:
        print(" " * num_esp + "*" + " " * num_esp_int + "*")
     else:
        print(" " * num_esp + "*")