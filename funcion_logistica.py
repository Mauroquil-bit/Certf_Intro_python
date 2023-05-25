"""
Función logística
Escribir un programa que lea un entero y calcule el valor de su función logística. 
Una función logística, o función sigmoide, es una función definida por la fórmula 
�
(
�
)
=
1
1
+
�
−
�
=
�
�
�
�
+
1
σ(x)= 
1+e 
−x
 
1
​
 = 
e 
x
 +1
e 
x
 
​
 
.

Imprima el resultado redondeado a 2 decimales.

Puede usar una constante igual o una especie de función de acceso directo, 
que se considera más precisa que o .math.e2.718281…math.exp(x)math.e ** xpow(math.e, x)

SUGERENCIA por 
avatar
 1234
1 / (1 + math.exp(-x)) es cómo obtienes el resultado, 
luego simplemente imprímelo y redondea a dos decimales
¿Te ha sido útil esta pista?
Ejemplo de entrada 1:

81
Ejemplo de salida 1:

1.0

"""

# # Escriba su código aquí
# import math
# x = int(input())
# print(round(1 / (1 + math.exp(-x)), 2))

# # Escriba su código aquí
import math
x = int(input())
print(round(1 / (1 + math.exp(-x)), 2))

