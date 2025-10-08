# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
El gobierno quiere otorgar becas de excelencia a los estudiantes con una media mínima de 8 puntos.
Además, solo pueden optar a la beca quienes tengan entre 17 y 21 años.

El programa debe pedir el nombre, la edad y la nota media, e indicar si el estudiante puede optar a la beca.
"""

# Solicitamos los datos del estudiante
nombre = input("Escriba su nombre: ").replace(".", "").replace("#", "").capitalize()
edad = int(input("¿Cuántos años tienes? "))
nota_media = float(input("¿Cuál es tu nota media? "))

# Comprobamos si cumple los requisitos de edad
if 17 <= edad <= 21:
    # Evaluamos la nota media
    if 8 <= nota_media <= 10:
        print(f"Enhorabuena, {nombre}! Por tu esfuerzo, eres apto para la beca.")
    elif 5 <= nota_media < 8:
        print(
            f"Lo sentimos, {nombre}. Tu nota media ({nota_media}) no alcanza el mínimo para la beca."
        )
    else:
        print(f"{nombre}, has suspendido. ¡Esfuérzate más!")
else:
    print(f"Lo siento, {nombre}. Estás fuera del rango de edad para optar a la beca.")
