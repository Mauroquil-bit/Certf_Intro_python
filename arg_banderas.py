"""
Argumentos como banderas
La tarea consiste en completar el código siguiente.

Agregue el argumento y use el parámetro. 
El valor del argumento debe ser si el argumento no aparece en la lista, 
y de lo contrario.--print_answeraction False True

import argparse

parser = argparse.ArgumentParser()

"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--print_answer', action='store_true')
args = parser.parse_args()

if args.print_answer:
    print(42)

# ¿Qué hace el código?
# El código crea un analizador de argumentos y agrega un argumento booleano.
#



