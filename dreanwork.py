
"""
Ejemplo 1

Enter the loan principal:
> 1000
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
> m
Enter the monthly payment:
> 150

It will take 7 months to repay the loan
Ejemplo 2

Enter the loan principal:
> 1000
What do you want to calculate? 
type "m" for number of monthly payments,
type "p" for the monthly payment:
> m
Enter the monthly payment:
> 1000

It will take 1 month to repay the loan
Ejemplo 3

Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
> p
Enter the number of months:
> 10

Your monthly payment = 100
Ejemplo 4

Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
> p
Enter the number of months:
> 9

Your monthly payment = 112 and the last payment = 104.
"""

# place `import` statement at top of the program
# En español: coloque la declaración de `importación` en la parte superior del programa
import math

# don't modify this code, otherwise, `principal` may not be available
# En español: no modifique este código, de lo contrario, `principal` puede no estar disponible
principal = int(input("Enter the loan principal:"))

# write your code here
# En español: escribe tu código aquí
print("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:""")
option = input()    # se lee la opción del usuario
if option == "m":   # si la opción es "m" entonces se calcula el número de pagos mensuales
    monthly_payment = int(input("Enter the monthly payment:"))  
    months = math.ceil(principal / monthly_payment) # math.ceil() redondea hacia arriba
    if months == 1: # si el resultado es 1, entonces se imprime en singular
        print("It will take 1 month to repay the loan") 
    else:       # si el resultado es mayor a 1, entonces se imprime en plural
        print(f"It will take {months} months to repay the loan")    
elif option == "p": # si la opción es "p" entonces se calcula el pago mensual
    months = int(input("Enter the number of months:"))  
    monthly_payment = math.ceil(principal / months) # math.ceil() redondea hacia arriba
    last_payment = principal - (months - 1) * monthly_payment   
    if monthly_payment == last_payment: # si el pago mensual es igual al último pago
        print(f"Your monthly payment = {monthly_payment}")  
    else:   # si el pago mensual es diferente al último pago
        print(f"Your monthly payment = {monthly_payment} and the last payment = {last_payment}.")   


# ==============================================================================





























