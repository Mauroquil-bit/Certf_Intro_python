"""
Equivalentes latinos

Imagine que tiene un programa de procesamiento de texto que no funciona con los caracteres ASCII. Aún así, debe usarlo y no tiene tiempo para corregir ese problema. Has decidido escribir otro programa que reemplazará todas las letras con ligaduras y marcas diacríticas con sus equivalentes del alfabeto latino. La lista de reemplazos es la siguiente:

é -> e ë -> e

á -> a
å -> aa
œ -> oe æ -> ae

Complete el código a continuación para que la función ( es una palabra clave utilizada para declarar funciones) tome una cadena con diacríticos y devuelva aquella en la que todos ellos han sido reemplazados por los equivalentes.normalizedef

Ejemplo de entrada 1:

Charlotte Brontë
Ejemplo de salida 1:

Charlotte Bronte

"""

name = input()

def normalize(name):
    new_name = name.replace("é", "e").replace("ë", "e").replace("á", "a").replace("å", "aa").replace("œ", "oe").replace("æ", "ae")
   
    return new_name

print(normalize(name))