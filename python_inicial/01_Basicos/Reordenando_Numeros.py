"""
Crea un script en el que el usuario introduzca un número de más de una cifra. El script debe
imprimir los componentes del número uno a uno por pantalla. Por ejemplo si el número introducido
es el 4532 por pantalla deberá imprimirse:
4
5
3
2
b. Crea un script que dado un numero entero de cuatro cifras calcula e imprima el número que
resulta de leer el número introducido de derecha a izquierda. Por ejemplo si el número introducido
es 4532, el output deberá ser 2354.
"""

# ====== Entrada número Usuario ======
numUsuario = input("Introduzca un número de más de una cifra ")

# ====== Bucle for para cada número, y hace salto automático ======
for num in numUsuario:
    print(num)
# ====== Revertir número ======
print(numUsuario[::-1])
