"""
Grado
Hay una serie de calificaciones que puede obtener en una prueba: A, B, C, D, F. Los porcentajes son los siguientes:

A: 90-100%

B: 80-90%

C: 70-80%

D: 60-70%

F: <60%

Determine la calificación que obtendrá un estudiante en función del puntaje 
del estudiante y el puntaje máximo.

Tenga en cuenta que el límite superior no está incluido en el rango, 
excepto para el grado A. Por ejemplo, un estudiante con 60% obtendrá D, 
con 70% o 79.9% - C, pero el puntaje más alto del 100% es solo A.

El formato de entrada:

Dos líneas: la primera con la puntuación de un alumno y la segunda con la máxima.

El formato de salida:

La calificación del estudiante.

SUGERENCIA por 
avatar
 Cuenta eliminada
Máx. / Puntuación * 100
¿Te ha sido útil esta pista?
Ejemplo de entrada 1:

75
100
Ejemplo de salida 1:

C
Ejemplo de entrada 2:

100
200
Ejemplo de salida 2:

F

"""

# # Escriba su código aquí
# score = int(input())
# max_score = int(input())
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# # Escriba su código aquí
score = int(input())
max_score = int(input())

# Transformar a porcentaje score y max_score
score = score / max_score * 100
max_score = max_score / max_score * 100

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

