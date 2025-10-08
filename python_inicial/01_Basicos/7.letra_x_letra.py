# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas
"""
Este ejercicio es un experimento que quise hacer.
Básicamente muestra un "Hola Mundo" letra por letra

"""
# ====== Importamos time ======
import time

# ====== Texto a mostrar letra por letra ======
texto = "Hola Mundo"
texto_revertido = ""

# ====== Usamos bucle for para ir letra por letra ======
for char in texto:
    time.sleep(1)
    print(char, end="")
