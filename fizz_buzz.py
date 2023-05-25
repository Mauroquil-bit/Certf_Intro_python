"""
FizzBuzz
FizzBuzz es un famoso desafío de código utilizado en entrevistas para probar habilidades básicas de programación. Es hora de escribir su propia implementación.

Imprima los números del 1 al 100 inclusive siguiendo estas instrucciones:

Si un número es múltiplo de 3, imprima en lugar de este número"Fizz"
Si un número es múltiplo de 5, imprima en lugar de este número"Buzz"
Para números que son múltiplos de 3 y 5, imprima "FizzBuzz"
Imprime el resto de los números sin cambios.
Genere cada valor en una línea independiente.
"""

# put your python code here
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")    
    elif i % 3 == 0:
        print("Fizz")    
    elif i % 5 == 0:
        print("Buzz")    
    else:
        print(i)

# ##############################################################################

# ¿Qué significa EOF en "SyntaxError: EOF inesperado durante el análisis"?

# EOF significa "End of File" (Fin de archivo).
# En otras palabras, 
# Python está diciendo que el analizador esperaba más código, pero no lo encontró.
#
# 
# ##############################################################################

# ¿Qué es un traceback en Python?

# Un traceback es un informe de error que muestra la secuencia de llamadas de funciones
# que condujeron al error.
#
#
# ##############################################################################

# Punteros adicionales
# A veces, el valor asociado de the no nos dice mucho sobre lo que realmente causó el error. 
# Para resolverlo por nosotros mismos, debemos averiguar dónde ocurrió exactamente el error. 
# ¿Cómo podemos hacerlo? SyntaxError

# La respuesta es: usando un traceback.
# Un traceback es un informe de error que muestra la secuencia de llamadas de funciones
# que condujeron al error.
#







