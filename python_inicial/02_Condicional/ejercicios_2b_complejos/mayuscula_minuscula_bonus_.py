# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
El programa permite al usuario introducir una letra (del alfabeto latino) y comprueba
si es mayúscula o minúscula.
"""

# Solicitamos una letra al usuario
letra = input("Introduzca una letra del alfabeto latino: ")

# Comprobamos si es mayúscula o minúscula
if letra.isupper():
    print(f"La letra '{letra}' es mayúscula.")
elif letra.islower():
    print(f"La letra '{letra}' es minúscula.")
else:
    print("El carácter introducido no es válido.")
