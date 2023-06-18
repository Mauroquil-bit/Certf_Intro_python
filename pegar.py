"""
Se le da una lista de números. Imprímalos juntos.

Propina: Establezca una línea vacía en uno de los argumentos, 
ya sea a o . Hay una solución con cada una de estas opciones.print()sepend

Ejemplo de entrada 1:

1 2 3 4 5 6 7 8 9
Ejemplo de salida 1:

123456789

"""

# numbers = [int(x) for x in input().split()]
# print all numbers without spaces

numbers = [int(x) for x in input().split()]
# print all numbers without spaces

print(*numbers, sep='')



# ################################################################

