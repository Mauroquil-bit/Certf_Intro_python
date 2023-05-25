# Description: Pago de anualidad


from math import ceil, floor, log, pow  # ceil: redondea hacia arriba, floor: redondea hacia abajo, log: logaritmo, pow: potencia


def calc(interest, principal=0.0, payment=0.0, periods=0.0):    # Función que calcula el pago de una anualidad
    rate = interest / (12 * 100)                                # Tasa de interés mensual 
    if not periods:                                             # Si no se especifica el número de periodos
        return ceil(log(payment / (payment - rate * principal), 1 + rate))  # 
    if not payment:                                                         # 
        return principal * rate * pow(1 + rate, periods) / (pow(1 + rate, periods) - 1) #
    if not principal:                                                                   # 
        return payment / (rate * pow(1 + rate, periods) / (pow(1 + rate, periods) - 1)) #

# choice es la variable que contiene la opción elegida por el usuario
choice = input('What do you want to calculate?\n'
               'type "n" - for count of months,\n'
               'type "a" - for annuity monthly payment,\n'
               'type "p" - for credit principal:\n')
if choice == 'n':   # Si el usuario elige calcular el número de meses   
    periods_finite = calc(principal=float(input('Enter credit principal:\n')),  # Se calcula el número de meses
                          payment=float(input('Enter monthly payment:\n')),     #  
                          interest=float(input('Enter credit interest:\n')))    # 
    print('You need',                                                 #         # Se imprime el resultado
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








