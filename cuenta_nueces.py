"""
Cuántas nueces quedarán después de la división
Problema del día
Siguiente problema en: 3h 3m 53s
Algunas ardillas encontraron algunas nueces y decidieron dividirlas por igual. 
Obtendrá el número de ardillas y el número de nueces como entrada en líneas separadas. 
Averigüe cuántas nueces quedarán después de que cada una de las ardillas 
tome el mismo número de nueces. Imprima el resultado.

Propina: La mejor manera de resolver esta tarea es usar el operador de módulo – %.
"""

# Solución
# ==============================================================================
# 1) Pedir al usuario el número de ardillas y el número de nueces
# 2) Calcular cuántas nueces le tocan a cada ardilla
# 3) Calcular cuántas nueces sobran
# 4) Imprimir el resultado
# ==============================================================================

a = int(input())
b = int(input())

print(b % a)

