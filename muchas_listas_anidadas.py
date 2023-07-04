"""
Muchas listas anidadas
Escribamos un programa que lea un entero positivo de la entrada 
y cree una lista anidada que contenga la lista interna repetida n veces.n[1, 2]

[PISTA] Use la comprensión de listas y recuerde qué argumentos se necesitan. [/SUGERENCIA]range()

Ejemplo de entrada 1:
5
Ejemplo de salida 1:
[[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]


Ejemplo de entrada 2:
2
Ejemplo de salida 2:
[[1, 2], [1, 2]]

"""

n = int(input())

my_list =  [[1, 2] for _ in range(n)]
print(my_list)