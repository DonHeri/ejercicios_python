# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
En uno de los cursos se ha dividido a una clase en dos grupos: A y B.

Para mezclar a los alumnos lo mejor posible:
- Las chicas con nombres que empiezan por las letras E–M van al grupo A; el resto al B.
- Los chicos con nombres que empiezan por A–H o R–Z también van al grupo A; el resto al B.

El programa debe preguntar el género y el nombre, y mostrar el grupo que corresponde.
"""

# Solicitamos los datos del usuario
genero = input("¿Eres chico o chica? [1 - chico | 2 - chica] ").strip().lower()
nombre = input(
    "¿Cómo te llamas? "
).title()  # Convertimos a formato título (primera letra mayúscula)

# Determinamos el grupo según las reglas
if genero in ("2", "chica"):
    if "E" <= nombre[0] <= "M":
        print(f"{nombre}, has sido seleccionada para el grupo A.")
    else:
        print(f"{nombre}, has sido seleccionada para el grupo B.")

elif genero in ("1", "chico"):
    if ("A" <= nombre[0] <= "H") or ("R" <= nombre[0] <= "Z"):
        print(f"{nombre}, has sido seleccionado para el grupo A.")
    else:
        print(f"{nombre}, has sido seleccionado para el grupo B.")

else:
    print("Entrada no válida. Vuelve a intentarlo.")
