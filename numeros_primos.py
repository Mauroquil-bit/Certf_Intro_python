"""
Números primos
En matemáticas, 
llamamos a un número primo natural si es mayor que 1 
y se puede dividir sin ningún resto solo por 1 y sí mismo:

2, 3, 5, 7, 11, 13, 17, ...

Cree una lista de todos los números primos hasta 1000 en el código siguiente. 
Simplemente guarde esta lista en una variable, no tiene que imprimir nada.prime_numbers

Utilice o compruebe si un número n deja un resto de cero 
cuando se divide por valores de 2 a n - 1 (inclusive).any()all()

"""

# prime_numbers = []
# for n in range(2, 1001):
#     if all(n % i != 0 for i in range(2, n)):
#         prime_numbers.append(n)
# print(prime_numbers)
#
# # ###################################################################

prime_numbers = []
for n in range(2, 1001):
    if all(n % i != 0 for i in range(2, n)):
        prime_numbers.append(n)
print(prime_numbers)

# ###################################################################

