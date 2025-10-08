# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
El programa solicita un número y una potencia, calcula el resultado y determina
si el número resultante es par o impar.
"""

# Solicitamos los valores al usuario
num = int(input("Introduzca un número: "))
potencia = int(input("Introduzca una potencia: "))

# Calculamos el resultado
resultado = num**potencia

# Comprobamos si el resultado es par o impar
if resultado % 2 == 0:
    print(f"El resultado de elevar {num} a {potencia} es par. Resultado: {resultado}")
else:
    print(f"El resultado de elevar {num} a {potencia} es impar. Resultado: {resultado}")
