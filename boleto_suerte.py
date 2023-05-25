"""
Boleto de la suerte
Los boletos de la suerte son una especie de entretenimiento matemático. 
Un boleto se considera afortunado si la suma de los primeros 3 dígitos 
es igual a la suma de los últimos 3 dígitos del número del boleto.
Se supone que debes escribir un programa que verifique si las dos sumas son iguales. 
El siguiente fragmento de código muestra si lo son y si no lo son."Lucky""Ordinary"

Sin embargo, faltan algunas partes del código. 
¡Rellena los espacios en blanco para que funcione!

Entrada: una cadena de 6 dígitos.

Salida: o (sin comillas)."Lucky""Ordinary"

Asegúrese de que NO está concatenando cadenas. Para ello, 
convierta cada dígito del número de ticket en un número entero. 
No olvides usar índices adecuados.

Ejemplo de entrada 1:

090234
Ejemplo de salida 1:

Lucky
Ejemplo de entrada 2:

123456
Ejemplo de salida 2:

Ordinary

"""

# Save the input in this variable

ticket = input()

# Add up the digits for each half
half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])


# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")


# Path: lucky_ticket.py

