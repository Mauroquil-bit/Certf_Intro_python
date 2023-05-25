"""
Favor
Carl te pide que cuentes la suma de los primeros k números naturales. 
Lea k de la entrada, luego sume números del 1 al k e imprima su respuesta.
Ejemplo de entrada 1:
7
Ejemplo de salida 1:
28
"""

# Escriba su código aquí
k = int(input())
print(k * (k + 1) // 2)

