"""
¡Es hora de hacer que nuestro juego sea interactivo! Ahora vamos a agregar la capacidad de que un usuario haga un movimiento. Para hacer esto, necesitamos dividir la cuadrícula en celdas. Supongamos que la celda superior izquierda tiene las coordenadas (1, 1) y la celda inferior derecha tiene las coordenadas (3, 3):

(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)

El programa debe pedir al usuario que introduzca las coordenadas de la celda donde desea hacer un movimiento.

En esta etapa, el usuario juega como X, no como O. Tenga en cuenta que la primera coordenada va de arriba a abajo y la segunda coordenada va de izquierda a derecha. Las coordenadas pueden incluir los números 1, 2 o 3.

¿Qué sucede si el usuario introduce coordenadas incorrectas? El usuario podría ingresar símbolos en lugar de números, o ingresar coordenadas que representen celdas ocupadas o celdas que ni siquiera están en la cuadrícula. Debe verificar la entrada del usuario y detectar posibles excepciones.


Objetivos
El programa debe funcionar de la siguiente manera:

Obtenga la cuadrícula inicial de 3x3 de la entrada como en las etapas anteriores. Aquí el usuario debe introducir 9 símbolos que representan el campo, por ejemplo, ._XXOO_OX_
Salida de esta cuadrícula 3x3 como en las etapas anteriores.
Solicite al usuario que realice un movimiento. El usuario debe introducir 2 números de coordenadas que representen la celda donde desea colocar su X, por ejemplo, .1 1
Analizar la entrada del usuario. Si la entrada es incorrecta, informe al usuario por qué su entrada es incorrecta:
Imprima si la celda no está vacía.
Imprimir si el usuario introduce símbolos no numéricos en la entrada de coordenadas.
Imprime si el usuario introduce coordenadas fuera de la cuadrícula del juego.
Siga solicitando al usuario que introduzca las coordenadas hasta que la entrada del usuario sea válida.This cell is occupied! Choose another one!You should enter numbers!Coordinates should be from 1 to 3!
Si la entrada es correcta, actualice la cuadrícula para incluir el movimiento del usuario e imprima la cuadrícula actualizada en la consola.
Para resumir, debe generar el campo 2 veces: una vez antes del movimiento del usuario (según la primera línea de entrada) y una vez después de que el usuario haya ingresado coordenadas válidas (luego debe actualizar la cuadrícula para incluir ese movimiento).

¡No elimine el código que escribió en la etapa anterior! Lo necesitará en la etapa final de este proyecto, por lo que ahora puede comentar una parte de él.


Ejemplos
El símbolo mayor que seguido de un espacio () representa la entrada del usuario. Tenga en cuenta que no es parte de la entrada.>

Ejemplo 1:

> X_X_O____
---------
| X   X |
|   O   |
|       |
---------
> 3 1
---------
| X   X |
|   O   |
| X     |
---------
Ejemplo 2:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------
Ejemplo 3:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 3 3
---------
|   X X |
| O O   |
| O X X |
---------
Ejemplo 4:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 2 3
---------
|   X X |
| O O X |
| O X   |
---------
Ejemplo 5:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 3 1
This cell is occupied! Choose another one!
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------
Ejemplo 6:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> one
You should enter numbers!
> one one
You should enter numbers!
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------
Ejemplo 7:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 4 1
Coordinates should be from 1 to 3!
> 1 4
Coordinates should be from 1 to 3!
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------

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










