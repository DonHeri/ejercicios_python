# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
El programa pide al usuario dos números y muestra por pantalla su división.
Si el divisor es cero, se muestra un mensaje de error.
"""

# Solicitamos los dos números
dividendo = int(input("Por favor, introduzca el dividendo: "))
divisor = int(input("Por favor, introduzca el divisor: "))

# Comprobamos que el divisor no sea cero
if divisor != 0:
    resultado = dividendo / divisor
    print(f"El resultado de la división es: {resultado}")
else:
    print(f"ERROR: no se puede dividir por {divisor}.")
