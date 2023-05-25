"""
Tipos
Digamos que hay un guión. Se necesitan exactamente cuatro argumentos, todos los cuales son numéricos. 
Se puede ejecutar desde la línea de comandos de esta manera: add_four_numbers.py

python3 add_four_numbers.py 25 17 808 9
Dentro del propio programa, los argumentos se leen primero desde la línea de comandos en la lista:args

# script 'add_four_numbers.py'

import sys  

args = sys.argv  
No ve la parte de importación del script, pero tiene acceso a , 
consulte a continuación (no importe el módulo usted mismo, es importante para las pruebas).args

Su tarea es acceder a los argumentos e imprimir el resultado de la adición. Por favor, 
conviértalo en un número entero.

Propina: ¿Recuerdas lo que almacena como primer elemento? ¿Y qué tipo tienen todos sus elementos?sys.argv
"""

# put your python code here
import sys

args = sys.argv
print(int(args[1]) + int(args[2]) + int(args[3]) + int(args[4]))

# ##############################################################################



