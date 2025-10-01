"""
En un restaurante el menú consta de las siguientes opciones:
Ensalada mixta   ————————   12 EU
Sopa de pescado    ———————   10 EU
Dorada al horno  ————————   18 EU
Arroz al curry  —————————   14 EU
Lasaña de carne     ———————   15 EU
Brownie de chocolate    —————    8 EU
Helado    ———————————    6 EU
Refrescos    ——————————    5,5 EU
Café    ————————————    3,5 EU
Escribe un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total
de la cuenta.
"""

# ====== Inicializamos precios del menú ======
precio_ensalada_mixta = 12
precio_sopa_pescado = 10
precio_dorada = 18
precio_arroz_curry = 14
precio_lasaña_carne = 15
precio_brownie_chocolate = 8
precio_helado = 6
precio_refrescos = 5.5
precio_cafe = 3.5

# ====== Preguntamos cuantos platos ha tomado ======
total_ensalada = int(input("Cuantas ensaladas mixtas ha tomado? "))
total_sopa_pescado = int(input("Cuantas sopas de pescado ha tomado? "))
total_dorada = int(input("Cuantas doradas al horno ha tomado? "))
total_arroz_curry = int(input("Cuanto arroz al curry ha tomado? "))
total_lasaña = int(input("Cuanta lasaña ha tomado? "))
total_brownie = int(input("Cuanto brownie ha tomado? "))
total_helado = int(input("Cuanto helado ha tomado? "))
total_refresco = int(input("Cuantos refrescos ha tomado? "))
total_cafe = int(input("Cuantos cafés ha tomado? "))

# ====== Desglose ======
total_menu = (
    (total_ensalada * precio_ensalada_mixta)
    + (total_sopa_pescado * precio_sopa_pescado)
    + (total_dorada * precio_dorada)
    + (total_arroz_curry * precio_arroz_curry)
    + (total_lasaña * precio_lasaña_carne)
    + (total_brownie * precio_brownie_chocolate)
    + (total_helado * precio_helado)
    + (total_refresco * precio_refrescos)
    + (total_cafe * precio_cafe)
)

# ====== Imprimir el total en pantalla ======
print(
    "Por todo lo que ha tomado, la cuenta suma un total de: ",
    total_menu,
    " euros. Muchas gracias y vuelva pronto",
)
