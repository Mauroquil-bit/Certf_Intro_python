"""
Ejemplo:

Entrada (el símbolo mayor que seguido del espacio representa la entrada del usuario, no es parte de la entrada):>

> 4
> -10
> 6
Salida (la suma de los cuadrados de los números 4, -10 y 6):

152
Ejemplo de entrada 1:

1
-3
5
-6
-10
13
4
-8
Ejemplo de salida 1:

340
"""

number_list = []
sum_ = 0
square_sum = 0

while True:
    number = int(input())
    sum_ += number
    number_list.append(number)
    if sum_ == 0:
        square_list = [num ** 2 for num in number_list]
        square_sum += sum(square_list)
        break
print(square_sum)



# ################################################################
