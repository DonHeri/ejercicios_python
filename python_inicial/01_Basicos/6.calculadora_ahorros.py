# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas
"""
Ahora que ya tienes soltura con los fundamentos de Python toca poner tus conocimientos en
práctica en un proyecto más extenso. El objetivo es crear un programa con el que puedas calcular
tus ahorros anuales. El programa deberá calcular cuánto puede ahorrar una persona dado sus
ingresos por hora, sus horas trabajadas y su gasto de vida semanal.
1. Primero haremos que el programa nos pida nuestro nombre y después imprima un saludo por
pantalla de tipo: 'Hola <Nombre>'
2. Guarda el dinero ganado por hora y las horas trabajadas en la semana en dos variables
diferentes
3. Multiplica ambas variables para obtener el salario semanal
4. Ahora calcula las ganancias anuales. Guarda el valor en una variable.
5. Ahora imprime por pantalla un mensaje del tipo: '<Nombre> tiene unas ganancias anuales de:
<cantidad> euros'
6. Pide los gastos semanales por pantalla y guárdalos en una variable.
7. Calcula el gasto anual
8. ¡Recuerda añadir comentarios sobre lo que esta haciendo cada parte del código!
9. Los ahorros anuales serán la resta entre lo ganado durante el año menos los gastos anuales.
10. Imprime los resultados por pantalla
¿Si el usuario decidiese trabajar a tiempo parcial (25 horas semanales) y decidiese reducir sus
gastos a 3/4 de lo que gastaba antes, tendría suficiente dinero para sus gastos?
(Pista: tan solo necesitas cambiar los valores de las variables de 'horas trabajadas por semana' y
'gastos semanales')

"""

# ====== 1.Nombre + Saludo ======
nombre_usuario = input("A continuación, dígame su nombre ")
saludo = "Hola " + nombre_usuario
print(saludo)

# ====== 2.Ganancias/Hora --- Total Horas Trabajadas ======
ganancias_hora = float(input("Cuánto gana por horas? "))
horas_trabajadas = float(input("Cuántas horas ha trabajado en total? "))

# ====== 3.Salario Semanal ======
salario_semanal = ganancias_hora * horas_trabajadas

# ====== 4.Ganancias Anuales ======
total_semanas = 365 / 7  # --Total semanas del año--
ganancias_anuales = salario_semanal * total_semanas

# ====== 5.Mensaje ======
print(
    nombre_usuario, " tiene unas ganancias anuales de: ", ganancias_anuales, " euros."
)

# ====== 6.Gastos Semanales ======
gastos_semanales = float(
    input(
        "Introduzca el total de gastos en la semana. [Comida | Luz | Agua | Alquiler | Ocio | Transporte | +...] -> "
    )
)
gastos_semanales = (
    3 / 4
) * gastos_semanales  # Para lo ultimo del ejercicio: 25Horas trabajadas y 3/4 de los gastos  OJO-EXTRA
# ====== 7.Total Gastos Anuales ======
gastos_anuales = gastos_semanales * total_semanas

# ====== 8.Ahorro Anual ======
ahorro = ganancias_anuales - gastos_anuales

# ====== 9.Desglose ======
print(
    "Desglose para ",
    nombre_usuario,
    "\nHoras Trabajadas Año: ",
    (horas_trabajadas * total_semanas),
    "\nGanancias Hora: ",
    ganancias_hora,
)
print(
    "Ganancias Anuales: ",
    ganancias_anuales,
    " euros ",
    "\nGastos Anuales: ",
    gastos_anuales,
    " euros",
)
print("Total Ahorrado en el año: ", ahorro, " euros")
