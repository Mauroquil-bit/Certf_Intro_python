"""
Lotería
Imagina que has comprado un montón de boletos de lotería y has anotado sus números en la lista. 
Ahora, es hora de averiguar si tiene un boleto ganador.

Sabes que todos los boletos ganadores no son menos de 44. 
Rellena los campos vacíos en el código (estos) para comprobar si tienes al menos un boleto ganador....

"""

# As luck would have it
tickets = [11, 22, 33, 44, 55]
winning_tickets = [i >=  44 for i in tickets]
tickets_bool =  any(winning_tickets)

# tickets = [11, 22, 33, 44, 55]
# winning_tickets = [i >= 44 for i in tickets]
# tickets_bool = any(winning_tickets)




