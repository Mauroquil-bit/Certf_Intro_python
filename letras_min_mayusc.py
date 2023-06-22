"""
snake_case
Problema del día
Siguiente problema en: 13h 14m 53s
Dado que estamos aprendiendo Python, a veces puede ser útil convertir texto de a . El truco principal es encontrar el lugar correcto donde insertar un guión bajo. Hagamos una regla de que un guión bajo debe insertarse justo antes de una letra mayúscula, por lo que se convertiría en .lowerCamelCasesnake_caselowerCamelCase lower_camel_case

El formato de entrada:

Leer una palabra o una frase escrita en lowerCamelCase

El formato de salida:

Imprime las palabras en minúsculas y sepáralas con guiones bajos.
"""

# your code here
palabra = input()
palabra = list(palabra)
for i in range(len(palabra)):
    if palabra[i].isupper():
        palabra[i] = "_" + palabra[i].lower()
palabra = "".join(palabra)
print(palabra)

# Path: letras_min_mayusc.py



