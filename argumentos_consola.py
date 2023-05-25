"""
A continuación se muestra un módulo que cuenta el número de cadenas vacías en el archivo dado, 
a partir del índice de línea dado.count_empty.py

import sys 

args = sys.argv 
if len(args) == 3:
    file_name = args[1]
    start = int(args[2])

    with open(file_name) as inp:
        counter = 0
        for i, line in enumerate(inp):
            if i < start:
                continue
            if not line.strip():
                counter += 1

    print(counter)
else:
    print("The number of passed arguments is incorrect. ")
¿Cómo lo ejecutarías desde la línea de comandos? 
Supongamos que desea comprobar el archivo que está en el mismo directorio que el script y 
desea comenzar desde la línea con el índice 101.test.txt

Propina: No necesita mirar el código en detalle, 
solo necesita comprender qué argumentos toma el script.
"""

# python count_empty.py test.txt 101
#
# ##############################################################################

# ¿Qué es un módulo en Python?

# Un módulo es un archivo que contiene definiciones y declaraciones de Python.
# Los módulos nos permiten organizar el código de Python de manera lógica y reutilizable.

