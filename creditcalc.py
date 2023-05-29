import argparse
import math

# crear el objeto ArgumentParser
parser = argparse.ArgumentParser()

# agregar argumentos posicionales
parser.add_argument("--type", type=str, help="the type of payment: 'annuity' or 'diff' (differentiated)")
parser.add_argument("--principal", type=float, help="the credit principal")
parser.add_argument("--periods", type=int, help="the number of months needed to repay the credit")
parser.add_argument("--interest", type=float, help="the credit interest")
parser.add_argument("--payment", type=int, help="Monthly payment amount")

# analizar argumentos
args = parser.parse_args()

# calcular el interés mensual
# interest = args.interest / (12 * 100)

# calcular el pago diferenciado
if args.type == "diff":
    if args.principal is None or args.periods is None or args.interest is None:
        print("Incorrect parameters")
    else:
        interest = args.interest / (12 * 100)
        total = 0
        for m in range(1, args.periods + 1):
            diff_payment = math.ceil(args.principal / args.periods + interest * (args.principal - args.principal * (m - 1) / args.periods))
            total += diff_payment
            print(f"Month {m}: paid out {diff_payment}")
        print()
        if total - args.principal >= 0:
            print(f"Overpayment = {total - args.principal}")
        else:
            print("Incorrect parameters")

# calcular el pago anual
elif args.type == "annuity":
    if args.principal is None or args.periods is None or args.interest is None:
        print("Incorrect parameters")
    else:
        annuity_payment = math.ceil(args.principal * (interest * pow(1 + interest, args.periods)) / (pow(1 + interest, args.periods) - 1))
        total = annuity_payment * args.periods
        print(f"Your annuity payment = {annuity_payment}!")
        if total - args.principal >= 0:
            print(f"Overpayment = {total - args.principal}")
        else:
            print("Incorrect parameters")

    # calcular el principal del préstamo
    if args.principal is None:
        principal = math.floor(args.periods * (annuity_payment / (interest * pow(1 + interest, args.periods) / (pow(1 + interest, args.periods) - 1))))
        total = annuity_payment * args.periods
        print(f"Your credit principal = {principal}!")
        if total - args.principal >= 0:
            print(f"Overpayment = {total - args.principal}")
        else:
            print("Incorrect parameters")

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

# mostrar un mensaje de error si el usuario ingresa parámetros no válidos
else:
    print("Incorrect parameters")
