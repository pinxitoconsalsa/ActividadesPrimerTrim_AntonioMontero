"""Dibuja un ordinograma que lea un valor correspondiente a una distancia en millas marinas
y escriba la distancia en metros. Sabiendo que una milla marina equivale a 1.852 metros."""

millas_marinas = float (input("Escriba las millas que deseas convertir a metros: "))
metros = millas_marinas*1.852

print(f"{millas_marinas} milla marina equivale a: {metros} metros.")