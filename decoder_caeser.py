def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''                                               # 
    for c in s:                                             # 
        text += alpha[(alpha.index(c) + n) % len(alpha)]    # 
    print('Decoded text: "' + text + '"')

# decode_Caesar_cipher('Pmttw, ewztl!', 2)
# ¿Qué hace esta función?
#
# La función toma una cadena y un número como argumentos.
# La función toma una cadena y un número como argumentos y devuelve una cadena.

# ¿Qué hace esta función?
# La función toma una cadena y un número como argumentos y devuelve una cadena.
# ##############################################################################

# ¿Que hace s = s.strip()?
# Elimina los espacios en blanco del principio y el final de la cadena.
# 
# ##############################################################################
# 
# ¿Qué hace for c in s:                                             # 
#        text += alpha[(alpha.index(c) + n) % len(alpha)]    # 
#    print('Decoded text: "' + text + '"')?
# 
# Itera sobre la cadena y agrega el carácter codificado a la cadena de texto.
#
# ##############################################################################

