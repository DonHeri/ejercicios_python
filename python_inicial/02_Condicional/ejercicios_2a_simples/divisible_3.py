# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
El programa solicita un número al usuario y comprueba
si es divisible por 3.
"""

# Solicitamos un número al usuario
numero = int(input("Introduce un número: "))

# Comprobamos si es divisible entre 3
if numero % 3 == 0:
    print(f"El número {numero} es divisible por 3.")
else:
    print(f"El número {numero} no es divisible por 3.")
