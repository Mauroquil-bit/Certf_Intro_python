"""
Números pares
Escriba un programa que tome una lista de números, 
cree otra lista de números pares de la primera lista y la imprima.

Por ejemplo, si , 
entonces su programa debe imprimir la lista .my_numbers = [1, 2, 3, 4, 5][2, 4]

"""

# the following line reads the list from the input; do not modify it, please
my_numbers = [int(x) for x in input().split(" ")]

# work with the variable 'my_numbers'
my_numbers_pares = []
for n in my_numbers:
    if n % 2 == 0:
        my_numbers_pares.append(n)
print(my_numbers_pares)

# ###################################################################

