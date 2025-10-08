# Ejercicios de: Academia ConquerBlocks
# Realizados por: Heriberto Rojas

"""
Un ordenador tiene tres usuarios distintos (Alejandro, Naomi y Sergio) y un usuario invitado.

El programa debe pedir el nombre, limpiar posibles símbolos o puntos, y mostrar una
bienvenida personalizada si el usuario es conocido. En caso contrario, mostrará un saludo genérico.
"""

# Solicitamos el nombre del usuario
nombre = input("Introduce tu nombre: ")

# Limpiamos posibles símbolos o errores al escribir
nombre = nombre.replace(".", "").replace("#", "").lower()

# Usuarios del sistema
usuarios = {
    "alejandro": "Hola Alejandro, bienvenido al sistema.",
    "naomi": "Hola Naomi, bienvenida al sistema.",
    "sergio": "Hola Sergio, bienvenido al sistema.",
}

# Mostramos el saludo correspondiente
print(usuarios.get(nombre, "Hola, ¡bienvenido invitado!"))
