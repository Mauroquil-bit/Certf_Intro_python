"""
Función Copysign
Escribe un programa que tome dos números flotantes, 
x e y, e imprima x con el signo de y. 
Utilice la función copysign definida en el módulo de matemáticas.

Las variables x e y ya están definidas.

Ejemplo de entrada 1:

-43.9446830180227 87.41382942412145
Ejemplo de salida 1:

43.9446830180227
"""

# place `import` statement at top of the program
from math import copysign

# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))
# use the imported function here
print(copysign(x, y))




