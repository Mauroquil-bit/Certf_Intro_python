"""
Embellece tanto la salida como el código
La salida debe ser fácil de usar, 
pero la parte del código también es importante. 
El código bien estructurado y legible es muy importante para ser un buen programador. 
Ahora depende de usted decidir qué método de formato elegir.

Imagine que necesita componer una URL dinámica para cada usuario determinado con detalles específicos del usuario. 
Supongamos que desea enviar diferentes URL para cada usuario, 
dependiendo de su nombre y profesión. La base sería algo así como

"http://example.com/*apodo*/deseable/*profesión*/perfil", 
donde apodo y profesión son indicaciones de un usuario y son dinámicos.

Lea el apodo y la profesión del usuario de la entrada e imprima una URL específica del usuario. 
No se preocupe por ninguna regla de composición de las URL y simplemente use la entrada sin procesar para realizar la tarea.

"""

"""
Beautify both output and code
The output should be user-friendly, but the code part is also important. Well-structured and readable code is very important for being a good programmer. Now it's up to you to decide, which formatting method to choose.

Imagine you need to compose a dynamic URL for every certain user with user-specific details. Suppose, you want to send different URLs for every user, depending on their name and profession. The base would be something like

"http://example.com/*nickname*/desirable/*profession*/profile", where nickname and profession are prompts from a user and are dynamic.

Read the nickname and profession of the user from the input and print a user-specific URL. Don't bother about any rules of composing the URLs and just use raw input to accomplish the task.

"""

# Sample Input 1:
# John
# student
# Sample Output 1:
# http://example.com/John/desirable/student/profile
# Sample Input 2:
# Jack
# teacher
# Sample Output 2:
# http://example.com/Jack/desirable/teacher/profile

# Write your code here
nickname = input()
profession = input()
print("http://example.com/" + nickname + "/desirable/" + profession + "/profile")


##################################################################################

# Path: embellecer.py


