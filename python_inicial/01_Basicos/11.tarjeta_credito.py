# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas
"""
Crea un script que reciba como input un número de tarjeta de crédito e imprima por pantalla todos
los caracteres en forma de asterisco salvo los últimos cuatro. Si por ejemplo el número de tarjeta
es 1234 2345 3456 5678, el output deberá ser **** **** **** 5678.
"""

# ====== Entrada Tarjeta de credito ======
numero_tarjeta = input(
    "Introduzca los 16 dígitos de su tarjeta de crédito (xxxxxxxxxxxxxxxx)-> "
)
longitud = len(numero_tarjeta)

# ====== Extraemos los últimos 4 dígitos con slicking (cadena[inicio:fin]) ======
ultimos_cuatro = numero_tarjeta[-4:]

if (
    longitud == 16
):  # Quería jugar con el condicional, y asegurarme de que se introducen 16 dígitos
    print(
        "**** **** **** ", ultimos_cuatro
    )  # Imprimimos "*" + los ultimos cuatro dígitos
else:
    print("Error ❌")
