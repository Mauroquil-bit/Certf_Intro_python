"""
Ejemplo 6: calcule cuánto tiempo tomará pagar un préstamo con 500,000 de capital, pago mensual de 23,000 y 7.8% de interés

> python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!
Overpayment = 52000

"""


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


