"""
E ** x menos uno
Problema del día
Siguiente problema en: 3h 6m 32s
Escribe un programa que tome un entero x e imprima e (una constante matemática) 
elevada a la potencia de x, menos uno. Aquí está la fórmula: (
�
�
−
1
e 
x
 −1
).
Utilice la función definida en el módulo de matemáticas. 
Para hacerlo, lea atentamente su documentación.expm1()

La variable x ya está definida.
Ejemplo de entrada 1:

70
Ejemplo de salida 1:

2.515438670919167e+30

"""

# place `import` statement at top of the program
import math

# don't modify this code, otherwise, `x` may not be available
x = int(input())

# use expm1() here
print(math.expm1(x))

# ==============================================================================

