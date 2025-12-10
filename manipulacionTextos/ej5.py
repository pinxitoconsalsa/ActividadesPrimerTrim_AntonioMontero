"""Verificar si un carácter específico está en la cadena con un ciclo y comparaciones."""
while True:
    caracter = input("Introduce un caracter: ")
    
    if len(caracter)==1:
        break
    else:
        print("Solo puede introducir un caracter.")

print(f"El caracter a encontrar es {caracter}.")

cadena_completa = input("Introduce la cadena completa: ")

verificar = False
for c in cadena_completa:
    if c == caracter:
        verificar = True
        
if verificar == False:
    print(f"El caracter {caracter}, no se encuentra en la cadena `{cadena_completa}´")
else:
    print(f"El caracter {caracter}, se encuentra en la cadena `{cadena_completa}´")