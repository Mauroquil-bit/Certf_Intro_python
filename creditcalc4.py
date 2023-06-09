"""

Objectives
In this stage, you are going to implement the following features:

Calculation of differentiated payments. To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.
Ability to calculate the same values as in the previous stage for annuity payment (principal, number of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.
Handling of invalid parameters. It's a good idea to show an error message if the user enters invalid parameters (they are discussed in detail below).
The final version of your program is supposed to work from the command line and parse the following parameters:

--type indicates the type of payment: "annuity" or "diff" (differentiated). If --type is specified neither as "annuity" nor as "diff" or not specified at all, show the error message.
> python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters
--payment is the monthly payment amount. For --type=diff, the payment is different each month, so we can't calculate months or principal, therefore a combination with --payment is invalid, too:
> python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters
--principal is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.
--periods denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.
--interest is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided. These parameters are incorrect because --interest is missing:
> python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters
You may have noticed that for differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (the user will be calculating the number of payments, the payment amount, or the loan principal). Thus, you should also display an error message when fewer than four parameters are provided:

> python creditcalc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters
You should also display an error message when negative values are entered:

> python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters
The only thing left is to compute the overpayment: the amount of interest paid over the whole term of the loan. Voila: you have a real loan calculator!

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that this is not part of the input.

Example 1: calculating differentiated payments

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
In this example, the user wants to take a loan with differentiated payments. You know the principal, the count of periods, and interest, which are 1,000,000, 10 months, and 10%, respectively.

The calculator should calculate payments for all 10 months. Let’s look at the formula above. In this case:

P=1000000
n=10
i=interest12∗100%=10%12∗100%=0.008333...

Now let’s calculate the payment for the first month:

D1=Pn+i∗(P−P∗(m−1)n)=100000010+0.008333...∗(1000000−1000000∗(1−1)10)=108333.333...

The second month (m=2):

D2=Pn+i∗(P−P∗(m−1)n)=100000010+0.008333...∗(1000000−1000000∗(2−1)10)=107500

The third month (m=3):

D3=Pn+i∗(P−P∗(m−1)n)=100000010+0.008333...∗(1000000−1000000∗(3−1)10)=106666.666...

And so on. You can see other monthly payments above.

Your loan calculator should output monthly payments for every month as in the first stage. Also, round up all floating-point values.
Finally, your loan calculator should add up all the payments and subtract the loan principal so that you get the overpayment.

Example 2: calculate the annuity payment for a 60-month (5-year) loan with a principal amount of 1,000,000 at 10% interest

> python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880
Example 3: fewer than four arguments are given

> python creditcalc.py --type=diff --principal=1000000 --payment=104000
Incorrect parameters.
Example 4: calculate differentiated payments given a principal of 500,000 over 8 months at an interest rate of 7.8%

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
Example 5: calculate the principal for a user paying 8,722 per month for 120 months (10 years) at 5.6% interest

> python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your loan principal = 800018!
Overpayment = 246622
Example 6: calculate how long it will take to repay a loan with 500,000 principal, monthly payment of 23,000, and 7.8% interest

> python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!
Overpayment = 52000

"""

import argparse
import math

parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment")
parser.add_argument("--principal", type=int, help="Principal amount")
parser.add_argument("--periods", type=int, help="Number of months")
parser.add_argument("--interest", type=float, help="Interest rate")
parser.add_argument("--payment", type=int, help="Monthly payment amount")
args = parser.parse_args()

if args.type is None:
    print("Incorrect parameters")
    exit()

if args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
    exit()

if args.interest is None:
    print("Incorrect parameters")
    exit()

if args.type == "diff":
    if args.principal is None or args.periods is None:
        print("Incorrect parameters")
        exit()
    else:
        for m in range(1, args.periods + 1):
            diff_payment = math.ceil(args.principal / args.periods + args.interest / 1200
                             * (args.principal - args.principal * (m - 1) / args.periods))
            total += diff_payment
            print(f"Month {m}: paid out {diff_payment}")
print()
print(f"Overpayment = {total - args.principal}")


elif args.type == "annuity":
    
    
    if args.principal is None:
        if args.payment is None:
            if args.periods is None:
                print("Incorrect parameters")
                exit()
            else:
                i = args.interest / 1200
                annuity_payment = math.ceil(args.periods * (i * math.pow(1 + i, args.periods) / (math.pow(1 + i, args.periods) - 1)))
                print(f"Your annuity payment = {annuity_payment}!")
                print(f"Overpayment = {annuity_payment * args.periods - args.principal}")
        else:
            if args.periods is None:
                print("Incorrect parameters")
                exit()
            else:
                i = args.interest / 1200
                credit_principal = math.floor(args.payment / (i * math.pow(1 + i, args.periods) / (math.pow(1 + i, args.periods) - 1)))
                print(f"Your credit principal = {credit_principal}!")
                print(f"Overpayment = {args.payment * args.periods - credit_principal}")
    else:
        if args.payment is None:
            if args.periods is None:
                print("Incorrect parameters")
                exit()
            else:
                i = args.interest / 1200
                annuity_payment = math.ceil(args.principal * (i * math.pow(1 + i, args.periods) / (math.pow(1 + i, args.periods) - 1)))
                print(f"Your annuity payment = {annuity_payment}!")
                print(f"Overpayment = {annuity_payment * args.periods - args.principal}")
        else:
            if args.periods is None:
                i = args.interest / 1200
                months = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
                years = months // 12
                months = months % 12
                if years == 0:
                    if months == 1:
                        print(f"You need {months} month to repay this credit!")
                    else:
                        print(f"You need {months} months to repay this credit!")
                elif years == 1:
                    if months == 0:
                        print(f"You need {years} year to repay this credit!")
                    elif months == 1:
                        print(f"You need {years} year and {months} month to repay this credit!")
                    else:
                        
                        print(f"You need {years} year and {months} months to repay this credit!")
                else:
                    if months == 0:
                        print(f"You need {years} years to repay this credit!")
                    elif months == 1:
                        print(f"You need {years} years and {months} month to repay this credit!")
                    else:
                        print(f"You need {years} years and {months} months to repay this credit!")
                print(f"Overpayment = {args.payment * months - args.principal}")
            else:
                print("Incorrect parameters")
                exit()
else:
    print("Incorrect parameters")
    exit()

# Path: creditcalc.py

# Finalmente,
# su calculadora de préstamos debe sumar todos los pagos y
# restar el capital del préstamo para que obtenga el sobrepago.

# Ejemplo de salida
# La salida del programa debe tener un formato similar al siguiente ejemplo:

# > python creditcalc.py --principal=1000000 --periods=60 --interest=10
# Your annuity payment = 21248!
# Overpayment = 274880

# > python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
# Month 1: payment is 108334
# Month 2: payment is 107500
# Month 3: payment is 106667
# Month 4: payment is 105834
# Month 5: payment is 105000
# Month 6: payment is 104167
# Month 7: payment is 103334
# Month 8: payment is 102500
# Month 9: payment is 101667
# Month 10: payment is 100834

# Overpayment = 45837

# > python creditcalc.py --principal=1000000 --payment=104000 --periods=8 --interest=10
# Your credit principal = 790499!
# Overpayment = 696497

# > python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
# You need 2 years and 3 months to repay this credit!
# Overpayment = 52000

# > python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
# Your annuity payment = 21248!
# Overpayment = 274880

# > python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# Your loan principal = 800018!
# Overpayment = 246622



