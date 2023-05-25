"""
Descripción
Pensemos en lo que una calculadora de préstamos debería ser capaz de hacer. 
En general, toma varios parámetros, como el capital y los intereses de un préstamo, 
calcula los valores que el usuario desea saber (por ejemplo, 
pago mensual o sobrepago) y los envía al usuario.

¿No está familiarizado con estos conceptos? No te preocupes, 
te las explicaremos en términos sencillos. 
El capital es la cantidad original de dinero que pide prestado. 
El interés es un cargo por pedir prestado ese dinero, 
generalmente calculado como un porcentaje del monto principal.

Objetivos
Comencemos imitando este comportamiento. 
Hay algunas variables preparadas en el código fuente: 
estos son mensajes de texto que nuestra calculadora de préstamos puede generar. 
En esta etapa, todo lo que necesita hacer es generarlos en el orden correcto.

Ejemplo
Salida:

Loan principal: 1000
Month 1: repaid 250
Month 2: repaid 250
Month 3: repaid 500
The loan has been repaid!

"""

loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
print(loan_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)


