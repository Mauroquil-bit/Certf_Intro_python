"""
Plurales
Alex escribió un programa que lee a y a de la entrada para crear frases como y . 
Desafortunadamente, la condición para los sustantivos plurales actualmente falta. 
Alex no sabe cómo usar las declaraciones if, pero tú sí. 
Ayuda a Alex a completar este programa.numberword"3 cats""1 dog"

La forma plural de una palabra generalmente termina con s. 
Todos los números, excepto 1, esperan la forma plural después de ellos, 
incluso cero: ."0 birds"
Las palabras que forman su plural no sumando s, 
NO aparecerán en las pruebas.
Indirecta
Ejemplo de entrada 1:
1
engineer
Ejemplo de salida 1:
1 engineer
Ejemplo de entrada 2:
12
student
Ejemplo de salida 2:
12 students
"""

# Escriba su código aquí
number = int(input())
word = input()

# write a condition for plurals
if number == 1:
    pass
else:
    word += "s"
    

print(number, word)
