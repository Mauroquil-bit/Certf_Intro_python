"""
Cálculo de S V P
Problema del día
Siguiente problema en: 
Pregunte al usuario sobre los parámetros de un paralelepípedo rectangular 
(3 enteros que representan la longitud, el ancho y la altura)
e imprima la suma de las longitudes de borde, su área de superficie total y el volumen, 
una respuesta por línea.

Suma de longitudes de todas las aristas:

�
=
4
(
un
+
�
+
�
)
s=4 a+b+c)

Superficie:

�
=
2
(
un
�
+
�
�
+
un
�
)
S=2(ab+BC+ac)

Volumen:

�
=
un
�
�
V=ABC

Ejemplo de entrada 1:

5
10
15
Ejemplo de salida 1:

120
550
750

"""

# # Escriba su código aquí
# a = int(input())
# b = int(input())
# c = int(input())
# print(4*(a+b+c))
# print(2*(a*b+b*c+a*c))
# print(a*b*c)

a = int(input())
b = int(input())
c = int(input())
print(4*(a+b+c))    
print(2*(a*b+b*c+a*c)) 
print(a*b*c)

