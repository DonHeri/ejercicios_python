"""
En la competición de skeleton de las olimpiadas de invierno hay tres finalistas. El cronómetro mide
los siguientes tiempos:

Hannah Neise:   8 minutos 3 segundos y 10 centésimas
Jackie Narracott:  12 minutos 7 segundos y 8 centésimas
Kimberley Bos:   9 minutos 14 segundos y 3 centésimas

1. Crea un script que pida los tiempos por pantalla para cada uno de los finalistas
2. Convierte los tiempos de minutos-segundos-centésimas a segundos
3. Sabiendo que la pista es de 100 metros calcula la velocidad media de cada uno de ellos en
metros por segundo.
4. Imprime los resultados por pantalla
"""

# ====== Entrada de tiempos ======
tiempoHannah = input(
    "Introduce el tiempo de la finalista Hannah (formato:minutos segundos centésimas) "
)
tiempoJackie = input(
    "Introduce el tiempo de la finalista Jackie (formato:minutos segundos centésimas) "
)
tiempoKimberley = input(
    "Introduce el tiempo de la finalista Kimberley (formato:minutos segundos centésimas) "
)

# ====== Ahora separamos minutos, segundo y centésimas ======
minutosHannah, segundosHannah, centesimasHannah = tiempoHannah.split()
minutosJackie, segundosJackie, centesimasJackie = tiempoJackie.split()
minutosKimb, segundosKimb, centesimasKimb = tiempoKimberley.split()

# ====== Pasamos todo a segundos ======
tiempoHannah = (
    float(minutosHannah) * 60 + float(segundosHannah) + float(centesimasHannah) * 0.01
)
tiempoJackie = (
    float(minutosJackie) * 60 + float(segundosJackie) + float(centesimasJackie) * 0.01
)
tiempoKimberley = (
    float(minutosKimb) * 60 + float(segundosKimb) + float(centesimasKimb) * 0.01
)

# ====== Velocidad Media ======
velHannah = tiempoHannah / 100
velJackie = tiempoJackie / 100
velKimb = tiempoKimberley / 100

# ====== Imprimimos Resultados ======
print(
    "La finalista Hannah Neise ha alcanzado una velocidad media de: ",
    velHannah,
    " m/s",
)
print(
    "La finalista Jackie Narracott ha alcanzado una velocidad media de: ",
    velJackie,
    " m/s",
)
print(
    "La finalista Kimberley Bos ha alcanzado una velocidad media de: ", velKimb, " m/s"
)
