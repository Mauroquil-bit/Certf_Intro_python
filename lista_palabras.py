"""
Una lista de palabras
Escriba un programa que tome una lista con palabras, 
cree una nueva lista de palabras que comiencen con la letra "a" en la primera lista y la imprima.

¡Algunas palabras pueden comenzar con la A mayúscula! Déjelos en su forma original en la lista resultante.

Por ejemplo, si , entonces su programa debe imprimir la lista 
.words = ['apple', 'pear', 'banana', 'Ananas']['apple', 'Ananas']

La lista con palabras ya está definida: puede acceder a ella utilizando la variable .words

[PISTA] Utilice el método string para capturar todas las palabras que comienzan con o . 
Como alternativa, cambie la palabra que marca a minúsculas a través de , 
pero tenga en cuenta que este cambio no debe ser permanente. [/SUGERENCIA]str.startswith(('a', 'A'))'a''A'str.lower()

"""

words = ['apple', 'pear', 'banana', 'Ananas']

# work with the variable 'words'
words_a = []
for w in words:
    if w.lower().startswith('a'):
        words_a.append(w)
print(words_a)


# ###################################################################



