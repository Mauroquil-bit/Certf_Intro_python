"""
snake_case

Ya que estamos aprendiendo Python, a veces puede ser útil convertir texto de lowerCamelCase a snake_case. El truco principal es encontrar el lugar correcto donde insertar un guión bajo. Hagamos una regla de que se debe insertar un guión bajo justo antes de una letra mayúscula, por lo que CamelCase más bajo se convertiría en lower_camel_case.

El formato de entrada:

Leer una palabra o una frase escrita en lowerCamelCase

El formato de salida:

Imprime las palabras en minúsculas y sepáralas con guiones bajos.

Propina: El método de cadena puede ser útil. Devuelve el valor si la cadena consta completamente de letras minúsculas, y de lo contrario. Por ejemplo:str.islower()TrueFalse

print("A".islower())
# False
print("a".islower())
# True
print("aA".islower())
# False
También puede utilizar el método string para convertir todas las letras de la cadena a minúsculas.lower()

print("lowerCamelCase".lower())
# "lowercamelcase"

Ejemplo de entrada 1:

python
Ejemplo de salida 1:

python
Ejemplo de entrada 2:

parselTongue
Ejemplo de salida 2:

parsel_tongue

"""

# my_string = input()
#
# new_string = ""
# for i, c in enumerate(my_string):
#     if c.isupper():
#         new_string += "_" + c.lower()
#     else:
#         new_string += c
# print(new_string.lstrip("_"))

# ###################################################################

my_string = input()

new_string = ""
for i, c in enumerate(my_string):
    if c.isupper():
        new_string += "_" + c.lower()
    else:
        new_string += c
print(new_string.lstrip("_"))

# ###################################################################

