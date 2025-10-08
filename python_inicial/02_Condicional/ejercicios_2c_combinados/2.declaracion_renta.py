# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros
al mes. Además los tramos impositivos de la renta anual son los siguientes:

RENTA                  TIPO IMPOSITIVO
Menos de 15.000 €      5%
Entre 15.000 y 25.000 € 15%
Entre 25.000 y 35.000 € 20%
Entre 35.000 y 60.000 € 30%
Más de 60.000 €        45%

El programa debe comprobar si eres susceptible de que se te aplique algún tipo impositivo y,
en caso afirmativo, mostrar cuál te corresponde.
"""

# Pedimos los datos al usuario
edad = int(input("¿Cuántos años tienes? "))
salario = int(input("¿Cuánto cobras mensualmente? "))

# Comprobamos si cumple las condiciones para tributar
puede_tributar = (edad >= 18) and (salario >= 1000)

if puede_tributar:
    # Calculamos la renta anual
    renta_anual = salario * 12

    # Determinamos el tipo impositivo según el tramo
    if renta_anual <= 15000:
        contributivo = renta_anual * 0.05
        print(
            f"Se te aplica un tipo contributivo del 5%. Pagas un total de {contributivo} euros anuales."
        )

    elif renta_anual <= 25000:
        contributivo = renta_anual * 0.15
        print(
            f"Se te aplica un tipo contributivo del 15%. Pagas un total de {contributivo} euros anuales."
        )

    elif renta_anual <= 35000:
        contributivo = renta_anual * 0.20
        print(
            f"Se te aplica un tipo contributivo del 20%. Pagas un total de {contributivo} euros anuales."
        )

    elif renta_anual <= 60000:
        contributivo = renta_anual * 0.30
        print(
            f"Se te aplica un tipo contributivo del 30%. Pagas un total de {contributivo} euros anuales."
        )

    else:
        contributivo = renta_anual * 0.45
        print(
            f"Se te aplica un tipo contributivo del 45%. Pagas un total de {contributivo} euros anuales."
        )

else:
    print("No eres susceptible de que se te aplique ningún tipo impositivo.")
