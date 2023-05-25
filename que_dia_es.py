"""
¿Qué día es?
Hoy en día, todo el mundo utiliza el Tiempo Universal Coordinado (UTC) 
para distinguir entre las zonas horarias. El UTC se considera el 0, 
y el resto de las zonas horarias se expresan utilizando compensaciones positivas o negativas del UTC. 
Por ejemplo, Londres está en la zona UTC+00:00 (o GMT) y Moscú está en la zona UTC+3:00.

Hay 14 compensaciones positivas (de UTC+1:00 a UTC+14:00) y 
12 compensaciones negativas (de UTC-12:00 a UTC-1:00). 
Esto también significa que a una hora determinada, 
se observan tres días calendario en el planeta. Por ejemplo, 
si ahora es domingo, 11:30 de la mañana en Londres, 
entonces en la zona horaria con +14:00 de compensación la gente ya está viviendo en el "día siguiente", 
lunes, porque su tiempo está 14 horas por delante de Londres.

Su tarea se establece de la siguiente manera:

el punto de referencia es el martes, 10:30 de la mañana en Londres (UTC+00:00)
Lea la cadena de entrada que contiene el número y el signo de este número 
(por ejemplo, +4, -10). Tenga en cuenta, sin embargo, 
que no habrá ninguna señal si el número es 0. El número es siempre un número entero.
Este número es el desplazamiento para alguna zona horaria.
Su programa debe calcular el día de la semana en la zona horaria para la que se le dio el desplazamiento. 
El punto de tiempo de referencia para sus cálculos se menciona anteriormente.
Salida el día de la semana en la zona horaria dada.
Por ejemplo, si la entrada es -11, entonces, relativamente a Londres, 
es "el día anterior" en esta zona horaria, es decir, todavía es lunes, 
pero si la entrada es +3, entonces es martes, lo mismo que en Londres.

El formato de entrada:

El valor del desplazamiento con el signo (por ejemplo, +3 o -9).

El formato de salida:

El día de la semana en esa zona horaria.

Ejemplo de entrada 1:

0
Ejemplo de salida 1:

Tuesday
Ejemplo de entrada 2:

-11
Ejemplo de salida 2:

Monday

"""

# Escriba su código aquí
from datetime import datetime, timedelta
from string import capwords

# print(capwords(input()))

def que_dia_es(zona_horaria):
    if zona_horaria == 0:
        return "Tuesday"
    else:
        return (datetime(2020, 3, 10, 10, 30) + timedelta(hours=zona_horaria)).strftime("%A")
    
# que_dia_es(int(input()))

print(que_dia_es(int(input())))

# print(que_dia_es(0))

# print(que_dia_es(0))



