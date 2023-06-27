"""
¿Cuántos días?
La lista de segundos es una lista de números que representan segundos. 
Convierta el número de segundos en días completos e imprima la lista que contiene estos valores. 
El número de días completos debe ser un valor.int

[PISTA] En caso de que lo hayas olvidado, hay 60 * 60 * 24 segundos en un día completo. 
En cuanto a obtener el número de días completos, use la división de piso (). [/SUGERENCIA]//

"""

seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here

days = []
for s in seconds:
    days.append(s // (60 * 60 * 24))
print(days)

# ###################################################################


