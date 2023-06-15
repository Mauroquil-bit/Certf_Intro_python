"""
Descripción
En la última etapa, calculemos los ingresos netos de la tienda. Para hacerlo, 
reste el personal y otros gastos de la suma total. Primero echemos un vistazo a los gastos de personal:

Personal

Sueldo

Cleaner

$850

Vendor

$1120

Manager

$1300

Loader

$900

Tenga en cuenta el hecho de que solo hay un miembro del personal en cada puesto. 
Por lo tanto, no necesita multiplicar los gastos de personal por 2 o 3. 
Solo hay un limpiador, un proveedor, y así sucesivamente.

Echa un vistazo a otros gastos:

Tipo de gastos

Costar

Electricity

$100

Municipal service

$90

Security

$30

En esta etapa, 
los gastos totales de personal y otros gastos se alimentan a su programa como dos entradas.

Objetivos
En esta etapa, su programa debe:

Imprima los nombres de los artículos y lo que ganó por cada uno de ellos;

Imprima las ganancias totales como antes;

Pregunte a los usuarios por los gastos de personal 
con la cadena y por otros gastos con la cadena;Staff expenses:Other expenses:

Calcule e imprima el ingreso neto como se muestra a continuación. 
Reemplácese con el ingreso neto real:0.0

Net income: $0.0
Ejemplos
El símbolo mayor que seguido de un espacio () representa la entrada del usuario. 
Tenga en cuenta que no es parte de la entrada: 
solo se usa para separar la entrada del usuario de la salida de su programa en los ejemplos de etapa, 
¡no necesita imprimir el letrero!> >

Ejemplo 1: salida al final de esta etapa (las cifras pueden variar):

Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80

Income: $7777.0
Staff expenses:
> 7777
Other expenses:
> 400
Net income: $-400

"""

# Write your code here
products = {'Bubblegum': 202,
            'Toffee': 118,
            'Ice cream': 2250,
            'Milk chocolate': 1680,
            'Doughnut': 1075,
            'Pancake': 80}

staff = {'Cleaner': 850,
            'Vendor': 1120,
            'Manager': 1300,
            'Loader': 900}

other_expenses = {'Electricity': 100,
            'Municipal service': 90,
            'Security': 30}


total_income = sum(products.values())
print('Earned amount:')
for key, value in products.items():
    print(f'{key}: ${value}')


print()
print(f'Income: ${total_income}')
print(input('Staff expenses:'))
#print(f'> {sum(staff.values())}')
print(input('Other expenses:'))
#print(f'> {sum(other_expenses.values())}')

print(f'Net income: ${total_income - sum(staff.values()) - sum(other_expenses.values())}')





# ################################################################

