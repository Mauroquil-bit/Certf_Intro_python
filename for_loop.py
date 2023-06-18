"""
Para bucle
Repetición de temas
Suerte 7
Lea la primera entrada: un número n. Luego lea la entrada n veces. 
Cada vez obtendrá un valor entero. Si es un múltiplo de 7 (se puede dividir por 7 sin un resto), 
imprime su cuadrado en una nueva línea. 
Tenga en cuenta que no es necesario realizar ningún cálculo en la primera entrada (la n).

[PISTA] Escriba n en alguna variable y luego, usando el bucle for, 
llame a la función input() exactamente n veces. Además, 
recuerde que la función input() devuelve cadenas y necesita ints. [/SUGERENCIA]

Ejemplo de entrada 1:

7
8
11
-49
0
3564
14
33
Ejemplo de salida 1:

2401
0
196

"""

# n = int(input())
# for i in range(n):
#     x = int(input())
#     if x % 7 == 0:
#         print(x * x)

"""
Ejemplo de entrada 2:

5
100
200
300
400
500
Ejemplo de salida 2:

10000
40000
90000
160000
250000
"""

n = int(input())
for i in range(n):
    x = int(input())
    if x % 7 == 0:
        print(x * x)

# ################################################################


