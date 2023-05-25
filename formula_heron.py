"""
Fórmula de Heron
Hace muchos años, cuando Paul fue a la escuela, 
no le gustaba usar la fórmula de Heron para calcular el área de un triángulo, 
porque consideraba que era muy complejo. 
Un día decidió ayudar a todos los estudiantes de su escuela escribiendo un programa 
que calculaba el área de un triángulo por sus tres lados.

Sin embargo, había un problema: como a Pablo no le gustaba la fórmula, 
no la memorizaba. 
Ayúdelo a terminar este acto de bondad y escriba el programa siguiendo la fórmula de Heron:
 
 es un medio perímetro del triángulo. En la entrada, el programa tiene enteros, 
 y la salida debe ser un número real correspondiente al área del triángulo.
NO redondee el resultado.

Ejemplo de entrada 1:

3
4
5
Ejemplo de salida 1:

6.0

"""

# put your python code here
import math
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)



