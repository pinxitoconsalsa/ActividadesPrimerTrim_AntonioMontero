"""Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador."""
while True:
    
    caracter = input("Dime el caracter que quiera contar: ")
    
    if len(caracter)==1:
        break
    else:
        print("Solo puede introducir un caracter.")
        
print(f"El caracter a contar es: {caracter}")

cadena_completa = input("Ingrese la cadena completa y realizaré el conteo del caracter: ")  

contador = 0

for i in cadena_completa:
    if i == caracter:
        contador = contador + 1 
        
print("-" * 20)
print(f"El caracter {caracter} aparece {contador} veces en la cadena `{cadena_completa}´")
print("-" * 20)