"""
Crea un script que muestre por pantalla el resultado de la siguiente operación aritmética:
 (3+2)
(=====)**2
 (2x5)

b. Escribe un programa que lea un entero positivo, n, introducido por el usuario y después
muestre por pantalla el resultado de la siguiente operación:
 n(n+1)
(======)
   2
c. Escribe un programa que pida al usuario dos números enteros y muestre por pantalla los
números de entrada, el cociente y el resto.
"""

# ====== 1era Operación ======
print(((3 + 2) / (2 * 5)) ** 2)

# ====== 2da Operación ======
n = int(input('Introduzca el valor de "n" para resolver la operación '))
print((n * (n + 1)) / 2)  # Output

# ====== 3ra Op - Entrada, cociente y resto ======
numero1 = int(input("Introduzca un primer número "))
numero2 = int(input("Introduzca un segundo número "))

print(numero1, "/", numero2)
print("Cociente = ", numero1 / numero2)
print("Resto = ", numero1 % numero2)
