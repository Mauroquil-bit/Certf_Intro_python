"""
Teoría
Cada nueva etapa de un proyecto es un paso adelante en la dificultad. 
La idea principal, sin embargo, sigue siendo la misma. 
Debe tomar su código desde la primera etapa y agregar nuevas características. 
Encuentre la descripción de estas características a continuación.

Descripción
Ha pasado un mes desde la apertura de su tienda. 
¡Calculemos las ganancias totales para este período! 
Conoces la cantidad total ganada por cada artículo:

Nombre del artículo

Cantidad ganada

Bubblegum

$202

Toffee

$118

Ice cream

$2250

Milk chocolate

$1680

Doughnut

$1075

Pancake

$80

Úsalo y encuentra el ingreso total en el primer mes.

Objetivos
En esta etapa, su programa debe:

Imprima la línea.Earned amount:

Imprima los nombres de los artículos y la cantidad ganada por cada uno de ellos;

Imprima las ganancias totales como se muestra a continuación. 
Sustitúyase por la suma total real:0.0

Income: $0.0
Ejemplo
Ejemplo 1: salida al final de esta etapa (las cifras pueden variar)

Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80

Income: $7777.0

"""
#
products = {'Bubblegum': 202,
            'Toffee': 118,
            'Ice cream': 2250,
            'Milk chocolate': 1680,
            'Doughnut': 1075,
            'Pancake': 80}

total_income = sum(products.values())
print('Earned amount:')
for key, value in products.items():
    print(f'{key}: ${value}')
print()
print(f'Income: ${total_income}')

# ################################################################
