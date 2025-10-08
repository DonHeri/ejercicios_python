# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
El programa solicita una contraseña al usuario. Si es correcta, muestra un mensaje de bienvenida.
Si es incorrecta, ofrece una segunda oportunidad. Si falla nuevamente, muestra un error y termina.

La validación no distingue entre mayúsculas y minúsculas.
"""

# Contraseña correcta almacenada
key = "contra1234"

# Solicitamos la contraseña al usuario
password = input("Introduzca la contraseña: ").lower()

# Comprobamos si es correcta
if password == key:
    print("¡Bienvenido! Ha iniciado sesión.")
else:
    # Segunda oportunidad
    password = input("Contraseña incorrecta. Inténtelo nuevamente: ").lower()
    if password == key:
        print("¡Bienvenido! Ha iniciado sesión.")
    else:
        print("Error. Ha agotado las oportunidades.")
