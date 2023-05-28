"""
Descripción
Finalmente, agreguemos a nuestra calculadora la capacidad de calcular pagos diferenciados. Haremos esto para el tipo de reembolso en el que el capital del préstamo se reduce en una cantidad constante cada mes. El resto del pago mensual se destina al pago de intereses y se reduce gradualmente durante el plazo del préstamo. Esto significa que el pago es diferente cada mes. Veamos la fórmula:

�
�
=
�
�
+
Yo
∗
(
�
−
�
∗
(
�
−
1
)
�
)
D 
m
​
 = 
n
P
​
 +I∗(P− 
n
P∗(m−1)
​
 )

Dónde:

�
�
D 
m
​
 
 = 
�
m
el pago diferenciado;

�
P
 = el principal del préstamo;

Yo
Yo
 = tipo de interés nominal. Esto suele ser 1/12 de la tasa de interés anual y es un valor flotante, no un porcentaje. Por ejemplo, si nuestra tasa de interés anual = 12%, entonces i = 0.01.

�
n
 = número de pagos. Este suele ser el número de meses en los que se realizarán los reembolsos.

�
m
 = mes de reembolso actual.

En esta etapa, el usuario tiene que introducir muchos parámetros, por lo que puede ser conveniente utilizar argumentos de línea de comandos. El módulo puede ayudarlo a analizarlos. Puede ejecutar su calculadora de préstamos a través de una línea de comandos como esta:argparse

python creditcalc.py
Mediante argumentos de línea de comandos, puede ejecutar el programa de esta manera:

python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Consulte la descripción y los ejemplos a continuación para obtener más detalles.

"""

import argparse
import math

# crear un objeto ArgumentParser
parser = argparse.ArgumentParser()

# agregar argumentos posicionales
parser.add_argument("--type", type=str, help="the type of payment: 'annuity' or 'diff' (differentiated)")
parser.add_argument("--principal", type=float, help="the credit principal")
parser.add_argument("--periods", type=int, help="the number of months needed to repay the credit")
parser.add_argument("--interest", type=float, help="the credit interest")

# analizar argumentos
args = parser.parse_args()

# calcular el interés mensual
interest = args.interest / (12 * 100)

# calcular el pago diferenciado
if args.type == "diff":
    if args.principal is None or args.periods is None or args.interest is None:
        print("Incorrect parameters")
    else:
        total = 0
        for m in range(1, args.periods + 1):
            diff_payment = math.ceil(args.principal / args.periods + interest * (args.principal - args.principal * (m - 1) / args.periods))
            total += diff_payment
            print(f"Month {m}: paid out {diff_payment}")
        print()
        print(f"Overpayment = {total - args.principal}")

# calcular el pago anual
elif args.type == "annuity":
    if args.principal is None or args.periods is None or args.interest is None:
        print("Incorrect parameters")
    else:
        annuity_payment = math.ceil(args.principal * (interest * pow(1 + interest, args.periods)) / (pow(1 + interest, args.periods) - 1))
        total = annuity_payment * args.periods
        print(f"Your annuity payment = {annuity_payment}!")
        print(f"Overpayment = {total - args.principal}")

    # calcular el principal del préstamo
    if args.principal is None:
        principal = math.floor(args.periods * (annuity_payment / (interest * pow(1 + interest, args.periods) / (pow(1 + interest, args.periods) - 1))))
        total = annuity_payment * args.periods
        print(f"Your credit principal = {principal}!")
        print(f"Overpayment = {total - principal}")

    # calcular el número de pagos
    if args.periods is None:
        periods = math.ceil(math.log(annuity_payment / (annuity_payment - interest * args.principal), 1 + interest))
        years = periods // 12
        months = periods % 12
        total = annuity_payment * periods
        if years == 0:
            print(f"You need {months} months to repay this credit!")
        elif years == 1 and months == 0:
            print(f"You need {years} year to repay this credit!")
        elif years == 1 and months == 1:
            print(f"You need {years} year and {months} month to repay this credit!")
        elif years == 1:
            print(f"You need {years} year and {months} months to repay this credit!")
        elif months == 0:
            print(f"You need {years} years to repay this credit!")
        elif months == 1:
            print(f"You need {years} years and {months} month to repay this credit!")
        else:
            print(f"You need {years} years and {months} months to repay this credit!")
        print(f"Overpayment = {total - args.principal}")

    # calcular el interés
    if args.interest is None:
        interest = (annuity_payment / (args.principal * pow(1 - 1 / (1 + interest), args.periods - 1)) - 1) * 12 * 100
        total = annuity_payment * args.periods
        print(f"Your credit interest = {interest}!")
        print(f"Overpayment = {total - args.principal}")

else:
    print("Incorrect parameters")


