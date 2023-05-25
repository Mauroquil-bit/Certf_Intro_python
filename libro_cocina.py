"""
Libro de cocina
Cualquier receta comienza con una lista de ingredientes. 
A continuación se muestra un extracto de un libro de cocina con los 
ingredientes para algunos platos. Escribe un programa que te diga qué 
receta puedes hacer en función del ingrediente que tengas.

El formato de entrada:

Un nombre de algún ingrediente.

El formato de salida:

Un mensaje que dice "¡hora de comer!", 
donde "comida" significa el plato que contiene este ingrediente. Por ejemplo, 
"¡hora de la pizza!" . Si el ingrediente aparece en varias recetas, 
escribe sobre todas ellas en el orden en que aparecen en el libro de cocina.

Ejemplo de entrada 1:

basil
Ejemplo de salida 1:

pasta time!
Ejemplo de entrada 2:

flour
Ejemplo de salida 2:

apple pie time!
chocolate cake time!
"""

# Escriba su código aquí
pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"


ingredient = input()

if ingredient in pasta:
    print("pasta time!")
if ingredient in apple_pie:
    print("apple pie time!")
if ingredient in ratatouille:
    print("ratatouille time!")
if ingredient in chocolate_cake:
    print("chocolate cake time!")
if ingredient in omelette:
    print("omelette time!")
#
#
#
