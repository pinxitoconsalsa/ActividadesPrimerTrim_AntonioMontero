"""Extraer subcadenas usando slicing (rebanado de cadenas sin usar listas)."""

cadena_principal = "La vida es preciosa"

#Solo indicando el final
cadenaFinal = cadena_principal[:7]
print(cadenaFinal) #output: La vida

#Solo indicando el principio
cadenaPrincipio = cadena_principal[11:]
print(cadenaPrincipio) #output: preciosa

#Indicando principio y final
cadenaPF = cadena_principal[8:10]
print(cadenaPF) #output: es

#Usando valores negativos
CadenaNeg = cadena_principal[-8:]
print(CadenaNeg) #output: preciosa

#invertir cadena
cadenaInv = cadena_principal[::-1]
print(cadenaInv)