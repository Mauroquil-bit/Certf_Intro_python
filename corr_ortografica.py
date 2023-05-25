"""
Corrector ortográfico
¡Whoa! Este problema requiere el conocimiento del tipo de colección. 
Si te sientes preparado para el desafío, prepárate, 
¡y buena suerte! De lo contrario, 
puede omitirlo por ahora y regresar en cualquier momento posterior.list
Escribe un corrector ortográfico simple que te diga 
si la palabra está escrita correctamente. 
Use el diccionario en el siguiente código: 
contiene la lista de todas las palabras escritas correctamente.
El formato de entrada:
Una sola línea con la "palabra".
El formato de salida:
Si la palabra está escrita correctamente, escriba Correcto, 
de lo contrario, Incorrecto.
Ejemplo de entrada 1:
aa
Ejemplo de salida 1:
Correcto
"""

# Escriba su código aquí
# Puede usar el código de la siguiente manera:
# print("Correcto" if word in words else "Incorrecto")
#
# Nota: La salida de este programa es:
# Correcto
# Incorrecto

# Path: corr_ortografica.py

dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]

word = input()

print("Correcto" if word in dictionary else "Incorrecto")

# Path: corr_ortografica.py