"""Crea un diamante hueco usando for (Hollow Diamond)"""

while True:
    try:
        # Pedimos la altura, que debe ser impar para un diamante simétrico.
        altura = int(input("Ingrese la altura que desea (recuerde que debe ser un número impar y positivo): "))
        
        # Validación de la entrada
        if altura <= 0 or altura % 2 == 0:
            print("La entrada debe ser impar y positiva.")
        else:
            break
    except ValueError:
        print("Debe ingresar un número entero.")

# 'n' es el número de la línea central o la mitad superior del diamante
# (ej: si altura=9, n=5)
n = (altura + 1) // 2 

# --- 1. PARTE SUPERIOR (Incluye la línea central) ---

# i va de 1 hasta n (ej: 1, 2, 3, 4, 5)
for i in range(1, n + 1):
    
    # a) Indentación (Espacios Iniciales)
    # n-i genera: n-1, n-2, ..., 0
    num_esp = n - i
    
    # b) Espacios Interiores
    # La longitud total de la fila es 2*i - 1. Para ser hueco, restamos los 2 asteriscos.
    # Genera: -1, 1, 3, 5, ...
    espacios_interiores_len = 2 * i - 3
    
    # Imprimir la línea
    espacios_inicio = " " * num_esp
    
    if espacios_interiores_len < 0:
        # Caso de la punta (i=1, espacios_interiores_len=-1). Imprime 1 solo *
        print(espacios_inicio + "*")
    else:
        # Caso de los bordes. Imprime * + espacios + *
        espacios_interiores = " " * espacios_interiores_len
        print(espacios_inicio + "*" + espacios_interiores + "*")


# --- 2. PARTE INFERIOR (No incluye la línea central) ---

# i va de n-1 hasta 1 (ej: 4, 3, 2, 1) para reflejar la parte superior
for i in range(n - 1, 0, -1):
    
    # a) Indentación (Espacios Iniciales)
    # n-i genera: 1, 2, 3, 4 (en el orden inverso al bucle)
    num_esp = n - i
    
    # b) Espacios Interiores
    # La misma fórmula genera la secuencia inversa: ..., 5, 3, 1, -1
    espacios_interiores_len = 2 * i - 3
    
    # Imprimir la línea
    espacios_inicio = " " * num_esp
    
    if espacios_interiores_len < 0:
        # Caso de la punta (i=1, espacios_interiores_len=-1). Imprime 1 solo *
        print(espacios_inicio + "*")
    else:
        # Caso de los bordes. Imprime * + espacios + *
        espacios_interiores = " " * espacios_interiores_len
        print(espacios_inicio + "*" + espacios_interiores + "*")
    

    