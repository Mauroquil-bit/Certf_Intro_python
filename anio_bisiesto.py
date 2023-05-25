"""
Año bisiesto
Escribe un programa que compruebe si un año es bisiesto.

Un año se considera bisiesto si es divisible por 4 y NO divisible por 100, 
o si es divisible por 400. Entonces, 2000 es bisiesto y 2100 no lo es.

Salida "Salto" u "Ordinario" dependiendo de la entrada.

Ejemplo de entrada 1:

2100
Ejemplo de salida 1:

Ordinary
Ejemplo de entrada 2:

2000
Ejemplo de salida 2:

Leap

"""

# Escriba su código aquí
# Puede usar el código de la siguiente manera:

# print("Leap" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "Ordinary")

# Nota: La salida de este programa es:
# Ordinary
# Leap

# Path: leap_year.py

year = int(input())

print("Leap" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "Ordinary")

# Path: leap_year.py

