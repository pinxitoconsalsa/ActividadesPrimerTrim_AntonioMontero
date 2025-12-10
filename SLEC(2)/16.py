def verificar_nota_diez():
    """
    Lee una secuencia de notas (0-10) terminada en -1 y verifica si alguna fue 10.
    No utiliza listas.
    """
    print("--- Verificador de Nota 10 ---")
    print("Ingresa notas entre 0 y 10. Finaliza la secuencia con el valor -1.")
    
    # Inicializamos la variable de control (flag)
    hubo_diez = False
    
    # Leemos la primera nota antes de entrar al bucle
    try:
        nota_str = input("Ingresa una nota (o -1 para terminar): ")
        nota = int(nota_str)
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")
        return # Terminamos la función si la primera entrada no es válida

    # Bucle principal que se ejecuta mientras la nota no sea el valor de terminación (-1)
    while nota != -1:
        # 1. Validar la nota
        if 0 <= nota <= 10:
            # 2. Verificar si la nota es 10
            if nota == 10:
                hubo_diez = True  # Activamos la bandera
                # Podemos terminar el bucle inmediatamente si encontramos un 10 (optimización)
                # break 
            
        else:
            print(f"La nota {nota} está fuera del rango válido (0-10). Se ignorará.")
        
        # 3. Leer la siguiente nota para la próxima iteración
        try:
            nota_str = input("Ingresa otra nota (o -1 para terminar): ")
            nota = int(nota_str)
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")
            # Si hay un error de entrada, forzamos la salida del bucle
            break

    # --- Resultado ---
    print("\n--- Resultado del Análisis ---")
    if hubo_diez:
        print("**¡SÍ!** Hubo al menos una nota con valor **10** en la secuencia.")
    else:
        print("**NO** hubo ninguna nota con valor 10 en la secuencia.")

# Ejecutar el programa
verificar_nota_diez()