"""
Cotangente
Problema del día
Siguiente problema en: 6h 6m 20s
Escriba un programa que lea un entero que represente un ángulo (en grados) e imprima su cotangente.

Calcule la cotangente como 
�
�
�
�
�
Yo
�
�
senφ
cosφ
​
 
 o 
1
�
un
�
�
tanφ
1
​
 
.

Redondee el resultado a 10 decimales.

ESCRIBE LOS COMENTARIOS MÁS IMPORTANTES DE CADA SECCIÓN.
"""
# import MÓDULOS
import math

# DEFINIR FUNCIONES
def cotangente(angulo):
    # calcular la cotangente
    cotangente = 1 / math.tan(math.radians(angulo))
    # redondear el resultado a 10 decimales
    cotangente = round(cotangente, 10)
    # imprimir el resultado
    print(cotangente)

# INGRESO Y SALIDA DE DATOS
# ingresar el ángulo
angulo = int(input())

# LLAMAR A LAS FUNCIONES
cotangente(angulo)

# FIN DEL PROGRAMA

# # Path: cotangente.py

# # Ejemplo de entrada
# # 45
# # Ejemplo de salida
# # 1.0
# # Ejemplo de entrada
# # 90
# # Ejemplo de salida
# # 6.1232339957e-17
# # Ejemplo de entrada
# # 309
# # Ejemplo de salida
# # -0.5773502692
# # Ejemplo de entrada
# # 360
# # Ejemplo de salida







