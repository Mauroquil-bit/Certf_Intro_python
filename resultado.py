"""
Comprensión de otros
Escriba un programa que convierta una lista determinada en una lista con valores binarios: 
1 o 0. Si el número en la lista inicial era mayor que 0, 
en la lista binaria debería haber 1, y si el número era menor o igual, en la nueva lista debe escribir 0. 
Naturalmente, use la comprensión de la lista e imprima el resultado.

Lista dada: una lista con números enteros, por ejemplo, .[5, 0, 4, -10]

Lista de salida: una lista que consta de unos y ceros, por ejemplo, .[1, 0, 1, 0]

"""

# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]

binary_list = [1 if n > 0 else 0 for n in old_list]

print(binary_list)
