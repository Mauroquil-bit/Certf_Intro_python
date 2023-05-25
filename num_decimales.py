"""
Número de decimales
Redondee el número de entrada al número requerido de decimales.

El formato de entrada:

Dos líneas: la primera con un número de punto flotante, 
la segunda con un número entero que representa el recuento decimal.

El formato de salida:

Una cadena con formato que contiene el número redondeado.

Olvídese de convertir los números 
de entrada y encerrar cada valor en una cadena formateada.NOT{}
Propina: Le recomendamos que utilice el formato de cadena, 
ya que las soluciones con función pueden no pasar las pruebas. Además, 
¡esto es exactamente de lo que se trata el tema!
Puede utilizar la especificación de formato 
para redondear el número al número requerido de decimales.round().{decimal_count}f

Ejemplo de entrada 1:

2.71828
3
Ejemplo de salida 1:

2.718
"""

# Write your code here
number = float(input())
decimal_count = int(input())
print(f"{number:.{decimal_count}f}")

# Sample Input 1:
# 2.71828
# 3
# Sample Output 1:
# 2.718
# Sample Input 2:
# 2.71828
# 0
# Sample Output 2:
# 3
# Sample Input 3:
# 2.71828
# 5
# Sample Output 3:
# 2.71828
# Sample Input 4:
# 2.71828
# 1
# Sample Output 4:
# 2.7
# #############################################################

# Path: num_decimales.py
