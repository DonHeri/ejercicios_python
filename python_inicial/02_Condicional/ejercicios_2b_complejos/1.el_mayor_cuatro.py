# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
El programa pide al usuario cuatro números diferentes y muestra
por pantalla cuál de ellos es el mayor.
"""

# Solicitamos los cuatro números
num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))
num3 = float(input("Introduzca el tercer número: "))
num4 = float(input("Introduzca el último número: "))

# Reordenamos los valores para encontrar el mayor
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num3 > num4:
    num3, num4 = num4, num3

# Mostramos el resultado
print(f"El número más alto es: {num4}")
