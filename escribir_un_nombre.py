"""
Escribir un nombre
Se le da una lista que contiene letras de un archivo . 
Imprímelos como una cadena con estos caracteres separados por guiones y con un signo de exclamación al final. 
¡Hazlo usando argumentos de la función!nameprint()

Por lo tanto, si las letras de la lista son ['K', 'A', 'T', 'E'], 
su programa debe imprimir la cadena 'K-A-T-E!'name

"""
name = ['M', 'A', 'R', 'C', 'O']
print("'", *name, sep="-", end="!'")



# ################################################################


# ¿Existe la función contraria a end='!'?
# Sí, existe. Es el argumento sep.
# Necesito agregar un apostrofe antes de la iteración:  print("'", *name, sep="-", end="!'")
# ¿Por qué necesito agregar un apostrofe antes de la iteración?
# Porque el asterisco desempaqueta la lista y la imprime sin comillas.
# ¿Por qué necesito agregar un apostrofe después de la iteración?
# Porque el argumento end agrega un signo de exclamación al final de la cadena.
# ¿Por qué necesito agregar un guión en el argumento sep?
# Porque el argumento sep agrega un guión entre los elementos de la lista.
# ¿Por qué necesito agregar un espacio en el argumento sep?



