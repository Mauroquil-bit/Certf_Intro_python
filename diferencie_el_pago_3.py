"""
Objetivos
En esta etapa, va a implementar las siguientes características:

Cálculo de pagos diferenciados. Para ello, el usuario puede ejecutar el programa especificando intereses, 
número de pagos mensuales y capital del préstamo.
Capacidad para calcular los mismos valores que en la etapa anterior para el pago de la anualidad (principal, 
número de pagos mensuales y monto del pago mensual). 
El usuario especifica todos los parámetros conocidos con argumentos de línea de comandos y un parámetro será desconocido. 
Este es el valor que el usuario desea calcular.
Manejo de parámetros no válidos. 
Es una buena idea mostrar un mensaje de error si el usuario introduce parámetros no válidos (se analizan en detalle a continuación).
Se supone que la versión final de su programa funciona desde la línea de comandos y analiza los siguientes parámetros:

--type indica el tipo de pago: o (diferenciado). 
Si no se especifica ni como ni como o no se especifica en absoluto, 
muestre el mensaje de error. "annuity""diff"--type"annuity""diff"
> python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters
--payment es el monto del pago mensual. Para , 
el pago es diferente cada mes, por lo que no podemos calcular meses o capital, por lo tanto, 
una combinación con tampoco es válida: --type=diff--payment
> python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters
--principal se utiliza para los cálculos de ambos tipos de pago. 
Puede obtener su valor si conoce el interés, el pago de la anualidad y el número de meses.
--periods Denota el número de meses necesarios para pagar el préstamo. Se calcula en función del interés, 
el pago de la anualidad y el capital.
--interest se especifica sin un signo de porcentaje. Tenga en cuenta que puede aceptar un valor de punto flotante. 
Nuestra calculadora de préstamos no puede calcular el interés, por lo que siempre debe proporcionarse. 
Estos parámetros son incorrectos porque faltan: --interest
> python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters
Es posible que haya notado que para pagos diferenciados necesitará 4 de 5 parámetros (excluyendo el pago),
 y lo mismo ocurre con los pagos de anualidades (el usuario calculará el número de pagos, 
 el monto del pago o el capital del préstamo). 
 Por lo tanto, también debe mostrar un mensaje de error cuando se proporcionan menos de cuatro parámetros:

> python creditcalc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters
También debe mostrar un mensaje de error cuando se introducen valores negativos:

> python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters
Lo único que queda es calcular el sobrepago: 
la cantidad de intereses pagados durante todo el plazo del préstamo. 
Voila: ¡tienes una calculadora de préstamos real!
"""

from math import ceil, floor, log, pow
import argparse

def calc(interest, principal=0.0, payment=0.0, periods=0.0):
    rate = interest / (12 * 100)
    if not periods:
        return ceil(log(payment / (payment - rate * principal), 1 + rate))
    if not payment:
        return principal * rate * pow(1 + rate, periods) / (pow(1 + rate, periods) - 1)
    if not principal:
        return payment / (rate * pow(1 + rate, periods) / (pow(1 + rate, periods) - 1))


parser = argparse.ArgumentParser(description='Credit Calculator')
parser.add_argument('--type', choices=['annuity', 'diff'], help='Type of calculation')
parser.add_argument('--principal', type=float, help='Credit principal')
parser.add_argument('--payment', type=float, help='Monthly payment')
parser.add_argument('--periods', type=int, help='Number of periods (months)')
parser.add_argument('--interest', type=float, help='Credit interest')

args = parser.parse_args()

if args.type == 'annuity':
    if args.periods is None:
        periods_finite = calc(interest=args.interest,
                              principal=args.principal,
                              payment=args.payment)
        print('You need',
              f'{periods_finite} months' if periods_finite < 12
              else (f'{int(periods_finite // 12)} year' if not periods_finite % 12
                    else f'{int(periods_finite // 12)} years and {ceil(periods_finite % 12)} months'),
              'to repay this credit!')
    elif args.payment is None:
        payment_finite = calc(interest=args.interest,
                              principal=args.principal,
                              periods=args.periods)
        print(f'Your annuity payment = {ceil(payment_finite)}!')
    elif args.principal is None:
        principal_finite = calc(payment=args.payment,
                                periods=args.periods,
                                interest=args.interest)
        print(f'Your credit principal = {floor(principal_finite)}!')


elif args.type == 'diff':
    if args.payment is not None:
        print('Incorrect parameters')
    else:
        total = 0
        for m in range(1, args.periods + 1):
            diff_payment = ceil(args.principal / args.periods + args.interest / 1200
                                * (args.principal - args.principal * (m - 1) / args.periods))
            total += diff_payment
            print(f'Month {m}: paid out {diff_payment}')
        print()
        print(f'Overpayment = {total - args.principal}')

else:
    print('Incorrect parameters')

# Path: creditcalc.py

"""
Wrong answer in test #5

Looks like your periods calculations aren't working properly. 
Correct years and overpayment are [ 2, 52000 ], but you output: ['2']

Please find below the output of your program during this failed test.

---

Arguments: --type=annuity --principal=500000 --payment=23000 --interest=7.8

You need 2 year to repay this credit!

"""

# ¿Como resuelvo el siguiente error?
# Wrong answer in test #5

# Looks like your periods calculations aren't working properly. 
# Correct years and overpayment are [ 2, 52000 ], but you output: ['2']

# Please find below the output of your program during this failed test.

# ---

# Arguments: --type=annuity --principal=500000 --payment=23000 --interest=7.8

# You need 2 year to repay this credit!


# Path: creditcalc.py



