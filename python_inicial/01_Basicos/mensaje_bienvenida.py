"""
MENSAJE DE BIENVENIDA:
El objetivo de este ejercicio es que crees un script que dado un nombre de usuario le de la
bienvenida con su nombre en el formato correcto
1. Escribe un programa que almacene el string estas usando python en una variable y luego
muestre por pantalla el contenido de la variable.
2. Amplía el programa para que pregunte el nombre de usuario en la terminal y después muestre
por pantalla el mensaje: ¡Hola, <nombre>, estas usando python! (<nombre> es el nombre que
el usuario hay introducido)
3. Usa una función interna de python que actúe sobre el string que has creado antes para que el
mensaje que imprima sea: ¡HOLA, <NOMBRE>, ESTAS USANDO PYTHON!
4. Cambia el script para que el mensaje se imprima al completo en minúsculas (usa de nuevo
una función interna de python)
5. Cambia el script para que, sin importar como introduzca el usuario el nombre, lo formatee para
que tenga el formato correcto, es decir con la primera letra en mayúsculas y las demás en
minúscula (Si el usuario introduce el nombre ferNanDO, el programa deberá formatear el
nombre a Fernando).
6. Amplía el script para que si por error el usuario introduce un nombre con un punto en medio, el
programa automáticamente lo borre (Si el usuario introduce el nombre Fern.ando, el programa
deberá formatear el nombre a Fernando)
7. Consigue que el mensaje final sea: '¡Hola, <Nombre>, estas usando Python!'
"""

# ====== Pido el nombre al usuario ======
nombre_usuario = input("¿Cómo te llamas? ")

# ====== Formatear nombre con .replace por si el usuario introduce un punto (".", "") ======
nombre_usuario = nombre_usuario.replace(".", "")

# ====== Escribimos mensaje en una variable ======
mensaje_inicial = (
    "¡Hola, " + nombre_usuario.title() + ", estás usando python!"
)  # Hemos añadimos .title() aquí para no modificar la variable

# ====== El ejercicio también nos pedía usar .lower() & .upper() para formatear el texto a minúsculas y mayúsculas respectivamente ======
print(mensaje_inicial.upper())

print(mensaje_inicial.lower())

# ====== Imprimimos el mensaje completo ======
print(mensaje_inicial)
