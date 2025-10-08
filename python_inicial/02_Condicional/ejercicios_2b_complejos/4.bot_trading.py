# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
Un bot de trading toma decisiones en función del precio de un producto financiero.

- Si el precio está por debajo de 100 dólares → COMPRAR
- Si el precio está entre 100 y 150 dólares (ambos incluidos) → HOLD
- Si el precio está por encima de 150 dólares → VENDER
"""

# Solicitamos el precio actual de la acción
precio = float(input("Introduzca el valor actual de la acción: "))

# Decisión del bot según el precio
if precio < 100:
    print("¡COMPRAR!")
elif 100 <= precio <= 150:
    print("¡HOLD!")
else:
    print("¡VENDER!")
