"""
El usuario es el gamemaster

Descripción
Nuestro programa debe ser capaz de mostrar la cuadrícula en todas las etapas del juego. 
Ahora vamos a escribir un programa que permite al usuario introducir una cadena 
que representa el estado del juego e imprime correctamente la cuadrícula del juego 3x3 en función de esta entrada. 
También agregaremos algunos límites alrededor de la cuadrícula del juego.

Objetivos
En esta etapa, escribirás un programa que:

Lee una cadena de 9 símbolos de la entrada y los muestra al usuario en una cuadrícula de 3x3. 
La cuadrícula sólo puede contener , y símbolos.XO_
Genera una línea de guiones por encima y por debajo de la cuadrícula, 
agrega un símbolo de barra vertical al principio y al final de cada línea de la cuadrícula 
y agrega un espacio entre todos los caracteres de la cuadrícula. ---------|
Ejemplos
El símbolo mayor que seguido de un espacio () representa la entrada del usuario. 
Tenga en cuenta que no es parte de la entrada.>

Ejemplo 1:

> O_OXXO_XX
---------
| O _ O |
| X X O |
| _ X X |
---------
Ejemplo 2:

> OXO__X_OX
---------
| O X O |
| _ _ X |
| _ O X |
---------
Ejemplo 3:

> _XO__X___
---------
| _ X O |
| _ _ X |
| _ _ _ |
---------

"""
# Se necesita una función que imprima la cuadrícula del juego 3x3 en función de la entrada del usuario.
# La cuadrícula sólo puede contener , y símbolos.XO_
# Genera una línea de guiones por encima y por debajo de la cuadrícula,
# agrega un símbolo de barra vertical al principio y al final de cada línea de la cuadrícula
# y agrega un espacio entre todos los caracteres de la cuadrícula. ---------|
# Ejemplos
# El símbolo mayor que seguido de un espacio () representa la entrada del usuario.
# Tenga en cuenta que no es parte de la entrada.>
# Ejemplo 1:
# > O_OXXO_XX
# ---------
# | O _ O |
# | X X O |
# | _ X X |
# ---------

# Ejemplo 2:
# > OXO__X_OX
# ---------
# | O X O |
# | _ _ X |
# | _ O X |
# ---------

# Ejemplo 3:
# > _XO__X___
# ---------
# | _ X O |
# | _ _ X |
# | _ _ _ |
# ---------

cadena = input("Ingrese una cadena de 9 símbolos: ")

def imprimir_cadena(cadena):
    print("---------")
    print("|", cadena[0], cadena[1], cadena[2], "|")
    print("|", cadena[3], cadena[4], cadena[5], "|")
    print("|", cadena[6], cadena[7], cadena[8], "|")
    print("---------")

imprimir_cadena(cadena)






# Path: usuario_gamemaster.py

# ###################################################################

