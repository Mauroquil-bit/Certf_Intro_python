"""
CapWords

En Python, los nombres de las clases (aprenderás sobre ellas en detalle más adelante) siguen la convención. 
Vamos a convertir la frase de entrada en consecuencia poniendo en mayúscula 
todas las palabras y deletreándolas sin guiones bajos en el medio.CapWords

El formato de entrada:

Una palabra o frase, con palabras separadas por guiones bajos, como nombres de funciones y variables en Python.

Es posible que desee cambiar el caso de las letras, ya que no están necesariamente en minúsculas.

El formato de salida:

El nombre escrito a la moda.CapWords

[PISTA] Utiliza para cambiar la primera letra de una palabra a mayúsculas y el resto de las letras a minúsculas. [/SUGERENCIA]word.capitalize()

Ejemplo de entrada 1:

BIRD
Ejemplo de salida 1:

Bird
Ejemplo de entrada 2:

my_class
Ejemplo de salida 2:

MyClass
"""


my_string = input()

new_string = ""

def lower_capitalized(my_string):
    word_lower = my_string.lower()
    word_capitalized = word_lower.capitalize()
    return word_capitalized



print(lower_capitalized(my_string))

# ###################################################################


# 
# 

#print(word_capitalized)



# ###################################################################






