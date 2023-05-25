"""
Una expresión compleja
Problema del día
Siguiente problema en: 15h 55m
Escriba un programa que tome un solo número entero n y, a continuación, realice las siguientes operaciones en el orden siguiente:

agrega n a sí mismo
multiplica el resultado por n
resta n del resultado
divide exactamente el resultado por n 
(eso significa que debe llevar a cabo una división entera).
A continuación, imprima el resultado de la división. 
El ejemplo se da a continuación:
8 + 8 = 16
16 * 8 = 128
128 - 8 = 120
120 // 8 = 15
La variable n ya está definida.
Ejemplo de entrada 1:
8
Ejemplo de salida 1:
15
"""

# Solución
# ==============================================================================
#Then print the result of the division. The example is given below:

#8 + 8 = 16
#16 * 8 = 128
#128 - 8 = 120
#120 // 8 = 15

# ==============================================================================

n = int(input())

# 1) agrega n a sí mismo
n1 = n + n
# 2) multiplica el resultado por n
n2 = n1 * n
# 3) resta n del resultado
n3 = n2 - n
# 4) divide exactamente el resultado por n (eso significa que debe llevar a cabo una división entera).
n4 = n3 // n

n = n4
print(n)
