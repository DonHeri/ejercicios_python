# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
En una hamburguesería han abierto la posibilidad de hacer pedidos online. Ofrecen básicamente
dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana.

Los ingredientes extra de la hamburguesa clásica son:
- Queso Idiazabal
- Bacon
- Huevo

Los ingredientes extra de la hamburguesa vegana son:
- Tofu
- Cebolla caramelizada

El programa debe preguntar el tipo de hamburguesa que elige el usuario, mostrarle los extras
disponibles según la opción, y finalmente imprimir su pedido.
"""

# Solicitamos el tipo de hamburguesa
eleccion = input(
    "Bienvenido a nuestro Restaurante Online.\n"
    "¿Qué va a pedir?\n"
    "[1] Hamburguesa Clásica\n"
    "[2] Hamburguesa Vegana\n"
    "[Escriba el número] > "
)

# Determinamos el tipo de hamburguesa y sus extras
if eleccion == "1":
    principal = "Hamburguesa Clásica"
    toppic = input(
        "¿Qué ingrediente extra desea?\n"
        "[1] Queso Idiazabal\n"
        "[2] Bacon\n"
        "[3] Huevo\n"
        "[Escriba el número] > "
    )

    if toppic == "1":
        toppic = "Queso Idiazabal"
    elif toppic == "2":
        toppic = "Bacon"
    elif toppic == "3":
        toppic = "Huevo"
    else:
        print("Por favor, elija solo uno de los tres toppings disponibles.")
        toppic = "sin topping"

elif eleccion == "2":
    principal = "Hamburguesa Vegana"
    toppic = input(
        "¿Qué ingrediente extra desea?\n"
        "[1] Tofu\n"
        "[2] Cebolla Caramelizada\n"
        "[Escriba el número] > "
    )

    if toppic == "1":
        toppic = "Tofu"
    elif toppic == "2":
        toppic = "Cebolla Caramelizada"
    else:
        print("Por favor, elija una de las dos opciones disponibles.")
        toppic = "sin topping"

else:
    print("Por favor, escriba solo el número de la opción deseada.")
    principal = "Sin selección"
    toppic = "N/A"

# Mostramos el resumen del pedido
print(
    f"\n¡Que aproveche!\nTu pedido se compone de: {principal}\n"
    f"Y has elegido {toppic} como topping.\n¡Vuelva pronto!"
)
