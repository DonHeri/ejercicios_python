# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas
"""
Una compañía de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM todoterreno.
Cada uno de estos coches tiene un precio de venta y el vendedor recibe una
comisión diferente por cada tipo de coche que ha vendido.

Suponga que los precios y las comisiones son:
RBM Serie 1:
precio: 20.000 EU, comisión: 3%

RMB Serie plus:
precio: 35.000 EU, comisión: 5%

RBM todoterreno:
precio: 60.000 EU, comisión: 7%
Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
mes  y que le devuelva la cantidad en euros a comisionar ese mes.
"""

# ====== Coches vendidos y su cantidad en euros ======
totalSerie1 = int(input("Cuantos RBM Serie 1 ha vendido? ")) * 20000
totalSeriePlus = int(input("Cuantos RMB Serie Plus ha vendido? ")) * 35000
totalTodoterreno = int(input("Cuantos RBM Todoterreno  ha vendido? ")) * 60000

# ====== Comisiones por ventas ======
comisionMes = (totalSerie1 * 0.03) + (totalSeriePlus * 0.05) + (totalTodoterreno * 0.07)

# ====== Imprimimos Comisionado del mes ======
print("Enhorabuena! Este mes se lleva usted: ", comisionMes, " euros en comisiones")
