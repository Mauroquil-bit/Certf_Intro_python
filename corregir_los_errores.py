"""
Dividir y unirse

Corregir los errores

Se supone que el siguiente código debe encontrar todas las direcciones de sitios web (, , ) en el texto de entrada. 
Sin embargo, no está terminado. 
Complete el código e imprima todas las direcciones en el orden en que aparecen en el texto, 
cada una en una nueva línea. 
Tenga en cuenta que puede ayudarlo a convertir todos los caracteres de la cadena a minúsculas.https://http://www.str.lower()

Ejemplo de entrada 1:

WWW.GOOGLE.COM uses 100-percent renewable energy sources and www.ecosia.com plants a tree for every 45 searches!
Ejemplo de salida 1:

WWW.GOOGLE.COM
www.ecosia.com

"""
text = input()
words = text.split()
for word in words:
    # finish the code here
    if word.lower().startswith("www.") or word.lower().startswith("http://") or word.lower().startswith("https://"):
        print(word)

# ###################################################################



