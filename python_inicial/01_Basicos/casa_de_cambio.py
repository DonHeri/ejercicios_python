"""
Una casa de cambios necesita construir un programa que dada una cantidad de euros introducida
por el usuario de el resultante en dólares.
1. Crea un script que reciba una cantidad de euros del usuario e imprima por pantalla el
correspondiente en dólares (considera una tasa de cambio donde 1 EU = 1.2 $)
2. La casa de cambios se queda un 10% en concepto de 'tasas de gestión'. Calcula el monto
recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de
dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal
forma que quede claro para el usuario.
"""

# ====== Entrada Euros Usuario. Convertimos a decimales para evitar error de tipos ======
cant_euros = float(input("¿Cuántos euros quiere cambiar?"))

# ====== Cambiamos a dolares e imprimimos en pantalla cantidad en dolares ======
cant_dolares = cant_euros * 1.20
print(cant_dolares)

# ====== La casa de cambio se queda con un 10% 'Tasas de gestión' ======
tasa_gestion = cant_dolares * 0.1
total_usuario = cant_dolares - tasa_gestion  # --Restamos la tasa al total--

# ====== Imprimimos el desglose por pantalla ======
print("Monto ingresado: ", cant_euros, " euros")
print("Cambio en dólares: ", cant_dolares, " dólares")
print("Tasa de gestión ", tasa_gestion, " dólares")
print(
    "Total recibido: ",
    total_usuario,
    " dolares. Muchas Gracias por confiar en nosotros!",
)
