"""
A través de la puerta
Supongamos que desea llevar una caja con dimensiones A × B × C (largo × ancho × alto) 
a través de la puerta con dimensiones X × Y (ancho × alto). 
Escribe un programa para comprobar si es posible.

El formato de entrada: 
La entrada comprende cinco cadenas con números en el siguiente orden:
A, B, C, X, Y. Si el tamaño de la puerta es mayor o igual 
a dos dimensiones cualesquiera de la caja, 
se considera que la caja se puede transportar.

El formato de salida:
Si la caja se puede llevar a través de la puerta, salida .
Si no se puede transportar, salida ."The box can be carried""The box cannot be carried"

SUGERENCIA por 
SRA.
 Michal Szubert
Comience con "si A < = X y B <= Y:". Luego, 2 elifs y más. Buena suerte
Ejemplo de entrada 1:

24
21
11
36
80
Ejemplo de salida 1:

The box can be carried
Ejemplo de entrada 2:

80
50
80
33
78
Ejemplo de salida 2:

The box cannot be carried

"""

# # Escriba su código aquí
# A = int(input())
# B = int(input())
# C = int(input())
# X = int(input())
# Y = int(input())
# if A <= X and B <= Y:
#     print("The box can be carried")
# else:
#     print("The box cannot be carried")

# Escriba su código aquí
A = int(input())
B = int(input())
C = int(input())
X = int(input())
Y = int(input())

if A <= X and B <= Y:
    print("The box can be carried")
elif A <= X and C <= Y:
    print("The box can be carried")
elif B <= X and C <= Y:
    print("The box can be carried")
else:
    print("The box cannot be carried")

