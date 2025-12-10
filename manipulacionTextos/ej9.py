"""Leer una cadena y contar cuántas vocales contiene."""
cadena = input("Ingrese una cadena de texto: ")

contador = 0
vocales = "aeiouAEIOU"
for i in cadena:
    if i in vocales:
        contador += 1

print(f"La cadena `{cadena}´, tiene {contador} vocales.")