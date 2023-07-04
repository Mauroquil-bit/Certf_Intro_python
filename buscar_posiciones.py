"""
Buscar posiciones
Escribe un programa que lea una secuencia de números de la primera línea y el número de la segunda línea. 
Luego debe generar todas las posiciones de en la secuencia numérica.xx

El recuento de posiciones comienza desde 0. 
En caso de que no esté en la secuencia, imprima la línea (comillas omitidas, minúsculas).x"not found"

Las posiciones deben mostrarse en una línea, en orden ascendente del valor.

[PISTA] Aquí hay un breve esquema: lea la entrada, 
luego cree una nueva lista para las posiciones y, 
al iterar sobre la lista de números, 
agregue todos los índices de las ocurrencias encontradas de esa lista 
(por ejemplo, puede usar una variable de contador para encontrarlas). 
Finalmente, únase a la lista de índices o imprima el mensaje. [/SUGERENCIA]x"not found"

Ejemplo de entrada 1:

5 8 2 7 8 8 2 4
8
Ejemplo de salida 1:

1 4 5
Ejemplo de entrada 2:

5 8 2 7 8 8 2 4
10
Ejemplo de salida 2:

not found

"""

my_list = [int(i) for i in input().split()]

my_number = int(input())

positions = []

for i, n in enumerate(my_list):
    if n == my_number:
        positions.append(i)

if positions:
    print(*positions)
else:
    print("not found")

# ###################################################################

