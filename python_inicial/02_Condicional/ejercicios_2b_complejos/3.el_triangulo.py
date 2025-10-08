# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
En una obra se necesita construir una estructura triangular para el tejado de una casa.
El ingeniero debe comprobar si, dadas las longitudes de tres piezas, es posible formar un triángulo.

Regla: la suma de dos lados debe ser mayor que el tercero (en todas las combinaciones).
"""

# Pedimos las medidas de los tres lados
lado1 = int(input("Introduzca la medida del primer lado: "))
lado2 = int(input("Introduzca la medida del segundo lado: "))
lado3 = int(input("Introduzca la medida del tercer lado: "))

import time

# Comprobamos si la estructura cumple la regla del triángulo
if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2):
    print("¡La estructura es válida!")
    time.sleep(1)
    print(f"Lado 1 = {lado1}\nLado 2 = {lado2}\nLado 3 = {lado3}")
    print("Se cumplen todas las condiciones para formar un triángulo.")
else:
    print("La estructura no es válida.")
