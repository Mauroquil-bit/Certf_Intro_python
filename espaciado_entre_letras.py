"""
Espaciado entre letras
Hagamos un poco de formato de texto. 
Lee una palabra de entrada e imprímela con un número indicado de espacios entre las letras. 
Hay dos entradas diferentes: 
una palabra en la primera línea y un número de espacios en la segunda línea.

Propina: Tenga en cuenta que el desempaquetado también funciona para cadenas. 
Y para obtener el número exacto de espacios, 
multiplica la cadena por ese número: ' ' * number_of_spaces

Ejemplo de entrada 1:

earnest
1
Ejemplo de salida 1:

e a r n e s t
Ejemplo de entrada 2:

Ernest
2
Ejemplo de salida 2:

E  r  n  e  s  t

"""

word = input()
number_of_spaces = int(input())
print(*word, sep=' ' * number_of_spaces)

# ################################################################

