"""Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre
el porcentaje de descuento realizado"""

precioArticulo=float (input("Dime el precio del artículo: "))
precioVenta=float (input("Dime el precio de venta: "))

diferencia=precioVenta * 100 / precioArticulo

if(precioArticulo>precioVenta): 
    porcentajeDescuento= 100 - diferencia
    print(f"El porcentaje de descuento es: {porcentajeDescuento}%")
else:
    porcentajeAumento= diferencia - 100
    print(f"El porcentaje de aumento es: {porcentajeAumento}%")
