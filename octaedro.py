"""
Octaedro
Un octaedro regular es una forma geométrica tridimensional, 
un poliedro con ocho caras iguales y doce aristas iguales. 
¿Alguna vez has visto dados de 8 caras? Eso es un octaedro regular. 
En esta tarea necesitas calcular su área y volumen.
Escriba un programa que lea un entero positivo 
que represente la longitud del borde del octaedro regular e imprima dos valores: 
su área y volumen (en ese orden), 
ambos redondeados a 2 decimales y divididos por un espacio.
Fórmula para calcular el área de un octaedro (a es la longitud del borde):

2
∗
3
∗
un
2
2∗ 
3
​
 ∗un 
2
 

Fórmula para calcular el volumen:

1
3
∗
2
∗
un
3
3
1
​
 ∗ 
2
​
 ∗un 
3
 
Ejemplo de entrada 1:
37
Ejemplo de salida 1:
4742.36 23878.05

"""

# Escriba su código aquí
a = int(input())
area = 2 * 3 ** 0.5 * a ** 2
volumen = 1 / 3 * 2 ** 0.5 * a ** 3
print(round(area, 2), round(volumen, 2))

#############################################################################

# ¿Qué es un octaedro?
# Un octaedro es un poliedro regular con ocho caras.
#
# ¿Qué es un poliedro?
# Un poliedro es un sólido geométrico tridimensional
# con caras planas y rectas.
#
# ¿Qué es un poliedro regular?
# Un poliedro regular es un poliedro cuyas caras son polígonos regulares.
#
# ¿Qué es un polígono regular?
# Un polígono regular es un polígono cuyos lados tienen la misma longitud
# y cuyos ángulos interiores tienen la misma medida.
#
# ¿Qué es un polígono?
# Un polígono es una figura plana de dos dimensiones
# con tres o más lados rectos y ángulos.
#
# ¿Qué es un ángulo?
# Un ángulo es una figura geométrica formada por dos rayos
# (líneas de media línea) que comparten un punto común.
#
# ¿Qué es un rayo?
# Un rayo es una línea que comienza en un punto
# y se extiende indefinidamente en una dirección.
#
# ¿Qué es una línea?
# Una línea es una serie de puntos que se extienden indefinidamente en ambas direcciones.
#
# ¿Qué es un punto?
# Un punto es un lugar en el espacio que no tiene dimensiones.
#
# ¿Qué es una dimensión?
# Una dimensión es una medida de longitud en una dirección particular.
#
# ¿Qué es una longitud?
# Una longitud es una medida de distancia.
#
# ¿Qué es una distancia?
# Una distancia es una medida de cuánto se separan dos puntos.
#
# Excelente COPILOT, ahora que sabemos qué es un octaedro,
# podemos continuar con el problema.
#
# ¿Qué es un problema?
# Un problema es una pregunta o situación que requiere una solución.
#
# ¿Qué hace esta línea de código? area = 2 * 3 ** 0.5 * a ** 2
# Esta línea de código calcula el área de un octaedro regular.
#
# ¿Qué hace esta línea de código? volumen = 1 / 3 * 2 ** 0.5 * a ** 3
# Esta línea de código calcula el volumen de un octaedro regular.
#
# ¿Qué es el área?
# El área es la cantidad de espacio dentro de los límites de una superficie plana.
#
# ¿Qué es el volumen?
# El volumen es la cantidad de espacio dentro de los límites de un objeto tridimensional.
#
# ¿Qué es un objeto tridimensional?
# Un objeto tridimensional es un objeto que tiene tres dimensiones: longitud, anchura y altura.
#
