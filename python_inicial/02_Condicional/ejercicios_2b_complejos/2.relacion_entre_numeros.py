# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
El programa solicita tres números diferentes y comprueba si alguno de ellos
es la suma de los otros dos.
"""

# Solicitamos los tres números
a = float(input("Introduzca el primer número: "))
b = float(input("Introduzca el segundo número: "))
c = float(input("Introduzca el tercer número: "))

# Comprobamos si alguno es la suma de los otros dos
if a + b == c:
    print(f"La suma de {a} + {b} = {c}")
elif a + c == b:
    print(f"La suma de {a} + {c} = {b}")
elif b + c == a:
    print(f"La suma de {b} + {c} = {a}")
else:
    print("Ninguno de los tres números es igual a la suma de los otros dos.")
