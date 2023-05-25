"""
Libro de cocina
Cualquier receta comienza con una lista de ingredientes. 
A continuación se muestra un extracto de un libro de cocina con los 
ingredientes para algunos platos. 
Escribe un programa que te diga qué receta puedes hacer en función del 
ingrediente que tengas.
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
ingredient = input()
if ingredient == "basil":
    print("pasta time!")
elif ingredient == "flour":
    