"""
Fahrenheit
Convierta la temperatura de Fahrenheit a Celsius en la función a continuación. Puedes usar esta fórmula:
�
∘
=
(
�
∘
−
32
)
×
5
9
C 
∘
 =(F 
∘
 −32)× 
9
5
​
 
Redondee el resultado devuelto a 3 decimales.
No tiene que manejar la entrada, solo implemente la función a continuación.
Además, asegúrese de que la función devuelve el valor. Por favor, NO imprima nada.

1) Redondear no requiere necesariamente que cree una variable y le asigne valor. El retorno puede generar el resultado de expresiones matemáticas. 
2) Redondee el número a 3 decimales usando la función " redondear (número, 3) "
3) Es un código de 2 líneas si lo haces bien.
"""

def fahrenheit_to_celsius(fahrenheit):
    celsius = int((fahrenheit - 32) * 5 / 9)
    return round(celsius, 3)

# Pruebas
print(fahrenheit_to_celsius(32))  # Debería ser 0
print(fahrenheit_to_celsius(-40))  # Debería ser -40
print(fahrenheit_to_celsius(212))  # Debería ser 100

# Nota: La salida de este programa es:
# 0.0
# -40.0
# 100.0

# Path: fahrenheit.py

