"""
Concurso de recitación de poesía
En un concurso de lectura de poesía, uno de los participantes recitó un poema de Alexander Blok, 
pero eligió la entonación incorrecta, 
por lo que el poema sonó como "¡La noche! ¡La farmacia! ¡La calle! ¡La farola sin sentido en la niebla!". 
En el poema original, el autor usaba comas entre los objetos y un punto al final de la oración.

Corrige el código para que los signos de puntuación 
sean correctos y ayuda al recitador a elegir la entonación correcta.

Cuidado con el punto y los espacios.


Ejemplo de entrada 1:

[“The night“, “the pharmacy”, “the street”, “the pointless lamppost in the mist”]
Ejemplo de salida 1:

The night, the pharmacy, the street, the pointless lamppost in the mist.

"""

poem = ['The night', 'the pharmacy', 'the street', 'the pointless lamppost in the mist']
print(poem[0], poem[1], poem[2], poem[3], sep=', ', end='.\n')

# ################################################################


