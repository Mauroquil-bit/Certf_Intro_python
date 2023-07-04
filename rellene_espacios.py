"""
Rellene los espacios en blanco
A continuación puede ver el código 
que elige algunos elementos de una lista y los anexa a otra:

for a in x:
    for el in a:
        if el > 0:
            els.append(el)
Complete los espacios en blanco en el código 
a continuación para que la comprensión de la lista produzca el mismo resultado que el código anterior.

"""

# here we create the initial list from the input, please do not modify this line
# x = json.loads(input())
# els = [el for __ in x for __ in a __ el > 0]

# here we create the initial list from the input, please do not modify this line
x = json.loads(input())

# write your list comprehension here
els = [el for  a in x for el in a if el > 0]



# ###################################################################


