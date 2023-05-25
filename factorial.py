"""
Factorial
El factorial del número N es el resultado de la multiplicación 
de todos los enteros positivos menores o iguales a N. Por ejemplo, 
el factorial de 3 es el producto de 3, 2, 1, es decir, ¡3! = 3 x 2 x 1 = 6. 
Ahora, su tarea es intentar escribir un programa que calcule el factorial 
del número de entrada usando el bucle while.
El formato de entrada:
El número N en rango de 1 a 100.
El formato de salida:
El factorial N!.
Ejemplo de entrada 1:
3
Ejemplo de salida 1:
6
"""
#
#

# ¿Qué es un número factorial?
# El factorial del número N es el resultado de la multiplicación 
# de todos los enteros positivos menores o iguales a N. Por ejemplo, 
# el factorial de 3 es el producto de 3, 2, 1, es decir, ¡3! = 3 x 2 x 1 = 6. 
# Ahora, su tarea es intentar escribir un programa que calcule el factorial 
# del número de entrada usando el bucle while.
#

num = int(input("Introduce un número: "))

factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print(factorial)

#
#
#


