# ====================================================
#  Archivo:         Experimento
#  Descripción:     Muestra Hola mundo letra por letra en pantalla- Importamos time y cada letra se muestra cada 1 segundo
#  Autor:           Heri
#  Fecha:           06/02/2025
# ====================================================

# ====== Importamos time ======
import time

# ====== Texto a mostrar letra por letra ======
texto = "Hola Mundo"
texto_revertido = ""

# ====== Usamos bucle for para ir letra por letra ======
for char in texto:
    time.sleep(1)
    print(char, end="")
