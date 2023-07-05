"""
Competición
Hoy estás participando en una competición de ajedrez. 
Obtendrás el estatus y la mayor cantidad de dinero si ganas todos los juegos. 
¡Hay mucho en juego!'winner'

Los resultados se almacenan en una lista. 
Complete los espacios en blanco 
en el código a continuación y determine cuánto dinero ganó.

NO necesita imprimir la respuesta.

"""


check = all([True, True, 0, 1, True])

if check:
    status = 'winner'
else:
    status = 'loser'

if status == 'winner':
    winning_sum = 100
else:
    winning_sum = 10

    