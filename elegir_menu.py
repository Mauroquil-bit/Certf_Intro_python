"""
Elección de elementos de listas anidadas
Imagine que la siguiente lista muestra una parte del menú de un café 
donde el primer elemento de cada lista anidada es el nombre de un plato, 
el segundo elemento es el número de personas a las que está dirigido el plato 
y el tercer número es su costo en la moneda local.

menu = [["pizza", 4, 20], ["soup", 1, 8], ["ice cream", 2, 4], ["toasts", 2, 10]]
Digamos que un cliente quiere seleccionar qué pedir usando Python y ha escrito el siguiente código:

what_to_order = [dish[0] for dish in menu if dish[1] >= 2 and dish[2] < 15]
print(what_to_order)
¿Qué resultado producirá esta expresión?

"""

menu = [["pizza", 4, 20], ["soup", 1, 8], ["ice cream", 2, 4], ["toasts", 2, 10]]

what_to_order = [dish[0] for dish in menu if dish[1] >= 2 and dish[2] < 15]
print(what_to_order)

# ###################################################################
