"""
Objetivos
En esta etapa, va a implementar las siguientes características:

Cálculo de pagos diferenciados. Para ello, el usuario puede ejecutar el programa especificando intereses, 
número de pagos mensuales y capital del préstamo.
Capacidad para calcular los mismos valores que en la etapa anterior para el pago de la anualidad (principal, 
número de pagos mensuales y monto del pago mensual). 
El usuario especifica todos los parámetros conocidos con argumentos de línea de comandos y un parámetro será desconocido. 
Este es el valor que el usuario desea calcular.
Manejo de parámetros no válidos. Es una buena idea mostrar un mensaje de error si el usuario introduce parámetros no válidos 
(se analizan en detalle a continuación).
Se supone que la versión final de su programa funciona desde la línea de comandos y analiza los siguientes parámetros:

--type indica el tipo de pago: o (diferenciado). 
Si no se especifica ni como ni como o no se especifica en absoluto, 
muestre el mensaje de error. "annuity""diff"--type"annuity""diff"

> python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters

--payment es el monto del pago mensual. Para , el pago es diferente cada mes, 
por lo que no podemos calcular meses o capital, por lo tanto, 
una combinación con tampoco es válida: --type=diff--payment

> python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters

--principal se utiliza para los cálculos de ambos tipos de pago. Puede obtener su valor si conoce el interés, el pago de la anualidad y el número de meses.
--periods Denota el número de meses necesarios para pagar el préstamo. Se calcula en función del interés, el pago de la anualidad y el capital.
--interest se especifica sin un signo de porcentaje. Tenga en cuenta que puede aceptar un valor de punto flotante. Nuestra calculadora de préstamos no puede calcular el interés, por lo que siempre debe proporcionarse. Estos parámetros son incorrectos porque faltan: --interest

> python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters

Es posible que haya notado que para pagos diferenciados necesitará 4 de 5 parámetros (excluyendo el pago), 
y lo mismo ocurre con los pagos de anualidades (el usuario calculará el número de pagos, 
el monto del pago o el capital del préstamo). Por lo tanto, 
también debe mostrar un mensaje de error cuando se proporcionan menos de cuatro parámetros:

> python creditcalc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters
También debe mostrar un mensaje de error cuando se introducen valores negativos:

> python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters

Lo único que queda es calcular el sobrepago: 
la cantidad de intereses pagados durante todo el plazo del préstamo. Voila: 
¡tienes una calculadora de préstamos real!

Ejemplos
El símbolo mayor que seguido de un espacio () representa la entrada del usuario. 
Tenga en cuenta que esto no forma parte de la entrada.>

Ejemplo 1: cálculo de pagos diferenciados

> python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834

Overpayment = 45837
En este ejemplo, el usuario quiere tomar un préstamo con pagos diferenciados. Usted conoce el capital, 
el recuento de períodos y los intereses, que son 1,000,000, 10 meses y 10%, respectivamente.

Ejemplo 2: calcular el pago de la anualidad para un préstamo a 60 meses (5 años) 
con un monto principal de 1,000,000 a un interés del 10%

> python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880

Ejemplo 3: se dan menos de cuatro argumentos

> python creditcalc.py --type=diff --principal=1000000 --payment=104000
Incorrect parameters.

Ejemplo 4: calcular pagos diferenciados dado un capital de 500,000 durante 8 meses a una tasa de interés de 7.8%

> python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
Month 1: payment is 65750
Month 2: payment is 65344
Month 3: payment is 64938
Month 4: payment is 64532
Month 5: payment is 64125
Month 6: payment is 63719
Month 7: payment is 63313
Month 8: payment is 62907

Overpayment = 14628

Ejemplo 5: calcular el capital de un usuario que paga 8.722 al mes durante 120 meses (10 años) al 5,6% de interés

> python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your loan principal = 800018!
Overpayment = 246622

Ejemplo 6: calcule cuánto tiempo tomará pagar un préstamo con 500,000 de capital, 
pago mensual de 23,000 y 7.8% de interés

> python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!
Overpayment = 52000


"""

from math import ceil, floor, log, pow

def calc(interest, principal=0.0, payment=0.0, periods=0.0):
    rate = interest / (12 * 100)
    if not periods:
        return ceil(log(payment / (payment - rate * principal), 1 + rate))
    elif not payment:
        return ceil(principal * ((rate * pow(1 + rate, periods)) / (pow(1 + rate, periods) - 1)))
    elif not principal:
        return floor(payment / ((rate * pow(1 + rate, periods)) / (pow(1 + rate, periods) - 1)))
    
def diff(interest, principal, periods):
    rate = interest / (12 * 100)
    total = 0
    for m in range(1, periods + 1):
        d = ceil((principal / periods) + rate * (principal - ((principal * (m - 1)) / periods)))
        total += d
        print(f"Month {m}: payment is {d}")
    print(f"\nOverpayment = {total - principal}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment")
    parser.add_argument("--payment", type=float, help="Monthly payment")
    parser.add_argument("--principal", type=float, help="Principal amount")
    parser.add_argument("--periods", type=int, help="Number of periods")
    parser.add_argument("--interest", type=float, help="Interest rate")
    args = parser.parse_args()
    if args.type == "diff" and args.principal and args.periods and args.interest:
        diff(args.interest, args.principal, args.periods)
    elif args.type == "annuity" and args.principal and args.periods and args.interest:
        print(f"Your annuity payment = {calc(args.interest, principal=args.principal, periods=args.periods)}!")
        print(f"Overpayment = {calc(args.interest, principal=args.principal, periods=args.periods) * args.periods - args.principal}")
    elif args.type == "annuity" and args.payment and args.periods and args.interest:
        print(f"Your loan principal = {calc(args.interest, payment=args.payment, periods=args.periods)}!")
        print(f"Overpayment = {args.payment * args.periods - calc(args.interest, payment=args.payment, periods=args.periods)}")
    elif args.type == "annuity" and args.principal and args.payment and args.interest:
        print(f"It will take {calc(args.interest, principal=args.principal, payment=args.payment)} years to repay this loan!")
        print(f"Overpayment = {args.payment * calc(args.interest, principal=args.principal, payment=args.payment) - args.principal}")
    else:
        print("Incorrect parameters")

if __name__ == "__main__":
    main()

#
#
#
#
#


