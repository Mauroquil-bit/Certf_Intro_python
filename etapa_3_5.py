"""
Trabajar en el proyecto. Etapa 3/5: ¿Qué hay en el campo?

¿Qué hay en el campo?

Descripción
En esta etapa, vamos a analizar el estado del juego para determinar 
si alguno de los jugadores ya ha ganado el juego o todavía está en curso, 
si el juego es un empate, o si el usuario ha entrado en un estado de juego imposible (dos ganadores, 
o con un jugador que ha hecho demasiados movimientos).

Objetivos
En esta etapa, su programa debe:

Tome una cadena introducida por el usuario e imprima la cuadrícula del juego como en la etapa anterior.
Analiza el estado del juego e imprime el resultado. Estados posibles:
Game not finished cuando ninguno de los lados tiene tres seguidos, pero la cuadrícula todavía tiene celdas vacías.
Draw Cuando ningún lado tiene un tres en una fila y la cuadrícula no tiene celdas vacías.
X wins cuando la cuadrícula tiene tres X seguidas (incluidas las diagonales).
O wins cuando la cuadrícula tiene tres O seguidas (incluidas las diagonales).
Impossible cuando la cuadrícula tiene tres X seguidas y tres O seguidas, 
o hay muchas más X que O o viceversa (la diferencia debe ser 1 o 0; 
si la diferencia es 2 o más, entonces el estado del juego es imposible).
En esta etapa, asumiremos que X u O pueden iniciar el juego.

Puede elegir si desea utilizar un espacio o un guión bajo para imprimir celdas vacías.

Ejemplos
El símbolo mayor que seguido de un espacio () representa la entrada del usuario. 
Tenga en cuenta que no es parte de la entrada.>

Ejemplo 1:

> XXXOO__O_
---------
| X X X |
| O O _ |
| _ O _ |
---------
X wins
Ejemplo 2:

> XOXOXOXXO
---------
| X O X |
| O X O |
| X X O |
---------
X wins
Ejemplo 3:

> XOOOXOXXO
---------
| X O O |
| O X O |
| X X O |
---------
O wins
Ejemplo 4:

> XOXOOXXXO
---------
| X O X |
| O O X |
| X X O |
---------
Draw
Ejemplo 5:

> XO_OOX_X_
---------
| X O   |
| O O X |
|   X   |
---------
Game not finished
Ejemplo 6:

> XO_XO_XOX
---------
| X O _ |
| X O _ |
| X O X |
---------
Impossible
Ejemplo 7:

> _O_X__X_X
---------
|   O   |
| X     |
| X   X |
---------
Impossible
Ejemplo 8:

> _OOOO_X_X
---------
|   O O |
| O O   |
| X   X |
---------
Impossible

"""

# write your code here
global cadena
cadena = input("Ingrese una cadena de 9 símbolos: ")

def imprimir_cadena(cadena):
    print("---------")
    print("|", cadena[0], cadena[1], cadena[2], "|")
    print("|", cadena[3], cadena[4], cadena[5], "|")
    print("|", cadena[6], cadena[7], cadena[8], "|")
    print("---------")

imprimir_cadena(cadena)

def analizar_cadena(cadena):
    if cadena.count("X") - cadena.count("O") > 1 or cadena.count("O") - cadena.count("X") > 1:
        print("Impossible")
    elif cadena.count("X") - cadena.count("O") == 1 or cadena.count("O") - cadena.count("X") == 1:
        if cadena.count("XXX") > 0 and cadena.count("OOO") > 0:
            print("Impossible")
        elif cadena.count("XXX") > 0:
            print("X wins")
        elif cadena.count("OOO") > 0:
            print("O wins")
        elif cadena.count("_") > 0:
            print("Game not finished")
        else:
            print("Draw")
    else:
        if cadena.count("XXX") > 0 and cadena.count("OOO") > 0:
            print("Impossible")
        elif cadena.count("XXX") > 0:
            print("X wins")
        elif cadena.count("OOO") > 0:
            print("O wins")
        elif cadena.count("_") > 0:
            print("Game not finished")
        else:
            print("Draw")

analizar_cadena(cadena)

# ###################################################################

