"""
Descripción
Ahora le enseñarás a tu bot a contar. ¡Se convertirá en un experto en números!

Objetivo
En esta etapa, programará el bot para que cuente 
desde 0 hasta cualquier número positivo que el usuario ingrese.

Ejemplo
El símbolo mayor que seguido de un espacio () representa la entrada del usuario. 
Tenga en cuenta que no es parte de la entrada.>

Ejemplo 1: un diálogo con la nueva versión del bot

Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
> Max
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
> 1
> 2
> 1
Your age is 22; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
> 5
0 !
1 !
2 !
3 !
4 !
5 !
Completed, have a nice day!
Nota: cada número comienza con una nueva línea y, después de un número, 
el bot debe imprimir el signo de exclamación.
Utilice la plantilla proporcionada para simplificar su trabajo. 
Puedes cambiar el texto si quieres, pero ten especial cuidado al contar números.

"""

"""
print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here

print('Completed, have a nice day!')
"""

print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

num = int(input())

i = 0

while i <= num:
    print(i, "!")
    i += 1

print('Completed, have a nice day!')

"""
Descripción
En esta etapa, su programa debe adivinar la edad del usuario
    y el número secreto que el usuario está pensando (el número secreto es un número entre 0 y 100,
    incluidos). El usuario piensa en estos números al comienzo del programa y no los cambia.

Objetivo
Su tarea es mejorar el bot para que pueda adivinar sus edades y números secretos
    utilizando una estrategia simple: adivinar los números en orden ascendente (de 0 a 100)
    para cada número, pregunte al usuario si es mayor que, menor que o igual al número que está adivinando.

Tenga en cuenta que el bot debe hacer preguntas estrictamente en este orden.
No debe hacer preguntas adicionales ni hacer preguntas fuera de este secuencia.

Cuando el programa adivina los números, debe decirlo en el siguiente formato:

    Tu edad es X años; ¡eso es un buen momento para comenzar a programar!
    Ahora adivinaré tu número secreto.
    Tu número secreto es Y; ¡Eso fue fácil! ¿Verdad?

Utilice la plantilla proporcionada para simplificar su trabajo.
Puede cambiar el texto si lo desea, pero tenga especial cuidado al imprimir números.

Ejemplo
El símbolo mayor que seguido de un espacio () representa la entrada del usuario.
Tenga en cuenta que no es parte de la entrada.>

Ejemplo 1: un diálogo con la nueva versión del bot

Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
> Max
What a great name you have, Max!
Let me guess your age.
Say me remainders of dividing your age by 3, 5 and 7.
> 1
> 2
> 1
Your age is 22; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
> 5
0 !
1 !
2 !
3 !
4 !
5 !
Completed, have a nice day!
Ejemplo 2: un diálogo con la nueva versión del bot

Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
> Max
What a great name you have, Max!
Let me guess your age.
Say me remainders of dividing your age by 3, 5 and 7.
> 2
> 1
> 2
Your age is 22; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
> 5
0 !
1 !
2 !
3 !
4 !
5 !
Completed, have a nice day!
Ejemplo 3: un diálogo con la nueva versión del bot

Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
> Max
What a great name you have, Max!
Let me guess your age.
Say me remainders of dividing your age by 3, 5 and 7.
> 1
> 2
> 1
Your age is 22; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
> 5
0 !
1 !
2 !
3 !
4 !
5 !
Completed, have a nice day!
"""




