"""
Escribe un programa que divida los números en dos listas dependiendo de si son mayores o menores que 5. 
No tienes que incluir el número 5 en sí.

Se ha leído una secuencia de números de la entrada para usted.

Ejemplo de entrada 1:

34567
Ejemplo de salida 1:

[3, 4]
[6, 7]

"""
# work with a list from this variable
numbers = [int(n) for n in input()]

# change the next two lines
less_than_5 = []
greater_than_5 = []

for n in numbers:
    if n < 5:
        less_than_5.append(n)
    else:
        if n == 5:
            pass
        else:
            greater_than_5.append(n)

# printing your results
print(less_than_5)
print(greater_than_5)