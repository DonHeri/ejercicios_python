# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
Por motivos de seguridad, una contraseña debe tener al menos:
- Una vocal en minúscula.
- Dos símbolos especiales diferentes (pueden ser solo * o #).

El programa solicita una contraseña e indica si cumple con los requisitos.
"""

# Solicitamos la contraseña al usuario
contra_usuario = input("Por favor, introduzca su contraseña: ").lower()

# Comprobamos si contiene los símbolos y al menos una vocal
tiene_simbolos = ("*" in contra_usuario) and ("#" in contra_usuario)
tiene_vocal = any(vocal in contra_usuario for vocal in "aeiou")

# Verificamos si cumple los requisitos de seguridad
if tiene_simbolos and tiene_vocal:
    print("¡Contraseña segura!")
else:
    print("Contraseña no segura.")
