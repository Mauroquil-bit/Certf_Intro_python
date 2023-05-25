"""
Ramo
A la florista Lillian le resulta más fácil arreglar flores cuando su número es impar. 
Entonces, si el número de flores en un ramo es uniforme, 
generalmente agrega una flor más. ¿Cómo replicaría este procedimiento en el código?
Asegúrese de sangrar su código correctamente: 
presionar el botón de flecha derecha una vez equivale a agregar 4 espacios para la sangría.
Para reordenar las líneas de código, 
puede usar las flechas hacia arriba y hacia abajo que se colocan a la derecha de cada línea de código, 
o arrastrarlas con el mouse.
"""

# Escriba su código aquí
num_flowers = int(input())
if num_flowers % 2 == 0:
    num_flowers += 1
print(num_flowers)

# Path: print_a_number.py

