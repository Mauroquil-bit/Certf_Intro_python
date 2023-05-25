"""
Triángulo o no triángulo
Lea tres ángulos dados en líneas de entrada separadas y verifique si forman un triángulo. Imprime la respuesta en el siguiente formato: "¡El triángulo es válido!" o "¡El triángulo no es válido!".

Ejemplo de entrada 1:

1
2
3
Ejemplo de salida 1:

The triangle is not valid!
Ejemplo de entrada 2:

60
60
60
Ejemplo de salida 2:

The triangle is valid!

"""

# Escriba su código aquí
# Puede usar el código de la siguiente manera:

# print("The triangle is valid!" if a + b + c == 180 else "The triangle is not valid!")

# Nota: La salida de este programa es:
# The triangle is not valid!
# The triangle is valid!

# Path: triangulo.py

a = int(input())
b = int(input())
c = int(input())

print("The triangle is valid!" if a + b + c == 180 else "The triangle is not valid!")

# Path: triangulo.py

