"""
¡Pelear!

Descripción
¡Nuestro juego está casi listo! Ahora vamos a combinar lo que hemos aprendido en las etapas anteriores para hacer un juego de tres en raya que dos jugadores pueden jugar desde el principio (con una cuadrícula vacía) hasta el final (hasta que haya un empate, o uno de los jugadores gane).

El primer jugador tiene que jugar como X y su oponente juega como O.

Objetivos
En esta etapa, debe escribir un programa que:

Imprime una cuadrícula vacía al principio del juego.
Crea un bucle de juego donde el programa le pide al usuario que ingrese las coordenadas de la celda, analiza el movimiento para verificar su corrección y muestra una cuadrícula con los cambios si todo está bien.
Termina el juego cuando alguien gana o hay un empate.
Necesitas generar el resultado final al final del juego. ¡Buena suerte!

Ejemplo
El símbolo mayor que seguido de un espacio () representa la entrada del usuario. Tenga en cuenta que no es parte de la entrada.>

Ejemplo 1.

---------
|       |
|       |
|       |
---------
> 2 2
---------
|       |
|   X   |
|       |
---------
> 2 2
This cell is occupied! Choose another one!
> two two
You should enter numbers!
> 1 4
Coordinates should be from 1 to 3!
> 1 1
---------
| O     |
|   X   |
|       |
---------
> 3 3
---------
| O     |
|   X   |
|     X |
---------
> 2 1
---------
| O     |
| O X   |
|     X |
---------
> 3 1
---------
| O     |
| O X   |
| X   X |
---------
> 2 3
---------
| O     |
| O X O |
| X   X |
---------
> 3 2
---------
| O     |
| O X O |
| X X X |
---------
X wins

"""

cadena = input("Ingrese una cadena de 9 símbolos: ")

def imprimir_cadena(cadena):
    print("---------")
    print("|", cadena[0], cadena[1], cadena[2], "|")
    print("|", cadena[3], cadena[4], cadena[5], "|")
    print("|", cadena[6], cadena[7], cadena[8], "|")
    print("---------")

imprimir_cadena(cadena)


def analizar_cadena(cadena):
    x = 0
    o = 0
    for c in cadena:
        if c == "X":
            x += 1
        elif c == "O":
            o += 1
    if abs(x - o) >= 2:
        print("Impossible")
    else:
        if cadena[0] == cadena[3] == cadena[6] == "X" and cadena[1] == cadena[4] == cadena[7] == "O":
            print("Impossible")

        elif cadena[0] == cadena[1] == cadena[2] == "X" or cadena[3] == cadena[4] == cadena[5] == "X" or cadena[6] == \
                cadena[7] == cadena[8] == "X" or cadena[0] == cadena[3] == cadena[6] == "X" or cadena[1] == cadena[4] == \
                cadena[7] == "X" or cadena[2] == cadena[5] == cadena[8] == "X" or cadena[0] == cadena[4] == cadena[
            8] == "X" or cadena[2] == cadena[4] == cadena[6] == "X":
            print("X wins")


        elif cadena[0] == cadena[1] == cadena[2] == "O" or cadena[3] == cadena[4] == cadena[5] == "O" or cadena[6] == \
                cadena[7] == cadena[8] == "O" or cadena[0] == cadena[3] == cadena[6] == "O" or cadena[1] == cadena[4] == \
                cadena[7] == "O" or cadena[2] == cadena[5] == cadena[8] == "O" or cadena[0] == cadena[4] == cadena[
            8] == "O" or cadena[2] == cadena[4] == cadena[6] == "O":
            print("O wins")

        elif cadena.count("_") > 0:
            print("Game not finished")
        else:
            print("Draw")


analizar_cadena(cadena)

def ingresar_mov(cadena):
    while True:
        try:
            x, y = input("Ingrese las coordenadas: ").split()
            x = int(x)
            y = int(y)
            if x > 3 or x < 1 or y > 3 or y < 1:
                print("Coordinates should be from 1 to 3!")
            elif cadena[(x - 1) * 3 + y - 1] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                break
        except ValueError:
            print("You should enter numbers!")
    return x, y

x, y = ingresar_mov(cadena)

def actualizar_cadena(cadena, x, y):
    cadena = cadena[: (x - 1) * 3 + y - 1] + "X" + cadena[(x - 1) * 3 + y:]
    return cadena

cadena = actualizar_cadena(cadena, x, y)

imprimir_cadena(cadena)

# ---------
# |       |
# |       |
# |       |
# ---------
# > 2 2
# ---------
# |       |
# |   X   |
# |       |
# ---------
# > 2 2
# This cell is occupied! Choose another one!
# > two two
# You should enter numbers!
# > 1 4
# Coordinates should be from 1 to 3!
# > 1 1

# ---------
# | O     |
# |   X   |
# |       |
# ---------
# > 3 3
# ---------
# | O     |
# |   X   |
# |     X |
# ---------
# > 2 1
# ---------
# | O     |
# | O X   |
# |     X |
# ---------
# > 3 1
# ---------
# | O     |
# | O X   |
# | X   X |
# ---------
# > 2 3
# ---------
# | O     |
# | O X O |
# | X   X |
# ---------
# > 3 2
# ---------
# | O     |
# | O X O |
# | X X X |
# ---------
# X wins

# ¿Cómo se puede mejorar el código anterior, incluyendo los ejemplos de jugadas?















