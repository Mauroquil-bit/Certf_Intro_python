from math import ceil, floor, log, pow


def calc(interest, principal=0.0, payment=0.0, periods=0.0):
    rate = interest / (12 * 100)
    if not periods:
        return ceil(log(payment / (payment - rate * principal), 1 + rate))
    if not payment:
        return principal * rate * pow(1 + rate, periods) / (pow(1 + rate, periods) - 1)
    if not principal:
        return payment / (rate * pow(1 + rate, periods) / (pow(1 + rate, periods) - 1))


choice = input('What do you want to calculate?\n'
               'type "n" - for count of months,\n'
               'type "a" - for annuity monthly payment,\n'
               'type "p" - for credit principal:\n')
if choice == 'n':
    periods_finite = calc(principal=float(input('Enter credit principal:\n')),
                          payment=float(input('Enter monthly payment:\n')),
                          interest=float(input('Enter credit interest:\n')))
    print('You need',
          f'{periods_finite} months' if periods_finite < 12
          else (f'{int(periods_finite // 12)} year' if not periods_finite % 12
                else f'{int(periods_finite // 12)} years and {ceil(periods_finite % 12)} months'),
          'to repay this credit!')
elif choice == 'a':
    payment_finite = calc(principal=float(input('Enter credit principal:\n')),
                          periods=float(input('Enter count of periods:\n')),
                          interest=float(input('Enter credit interest:\n')))
    print(f'Your annuity payment = {ceil(payment_finite)}!')
elif choice == 'p':
    principal_finite = calc(payment=float(input('Enter monthly payment:\n')),
                            periods=float(input('Enter count of periods:\n')),
                            interest=float(input('Enter credit interest:\n')))
    print(f'Your credit principal = {floor(principal_finite)}!')

else:
    print('Incorrect parameters')

# EJEMPLO DE EJECUCIÓN
# Ejemplo 2:
# calcular el pago de la anualidad para un préstamo a 60 meses (5 años)
# con un monto principal de 1,000,000 a un interés del 10%

# > python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
# Your annuity payment = 21248!
# Overpayment = 274880
# ################################################################################################################

# Ejemplo 3: se dan menos de cuatro argumentos

# > python creditcalc.py --type=diff --principal=1000000 --payment=104000
# Incorrect parameters.

# Ejemplo 4: se dan argumentos incorrectos

# > python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
# Incorrect parameters.

# Ejemplo 5: se dan argumentos incorrectos

# > python creditcalc.py --type=annuity --principal=100000 --periods=60 --interest=10
# Incorrect parameters.

# Ejemplo 6: se dan argumentos incorrectos

# > python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
# Incorrect parameters.

# Ejemplo 7: se dan argumentos incorrectos

# > python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# Incorrect parameters.

# Ejemplo 8: se dan argumentos incorrectos

# > python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
# Incorrect parameters.

