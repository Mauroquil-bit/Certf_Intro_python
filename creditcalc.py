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

elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
    exit()

elif args.interest is None:
    print("Incorrect parameters")
    exit()

elif args.type == "diff":
    if args.principal is None or args.periods is None:
        print("Incorrect parameters")
        exit()
    else:
        nominal_interest = args.interest / (12 * 100)
        total_payment = 0
        for m in range(1, args.periods + 1):
            payment = math.ceil(args.principal / args.periods + nominal_interest * (args.principal - args.principal * (m - 1) / args.periods))
            total_payment += payment
            print(f"Month {m}: payment is {payment}")
        print(f"\nOverpayment = {total_payment - args.principal}")
elif args.type == "annuity":
    if args.principal is None:
        nominal_interest = args.interest / (12 * 100)
        args.principal = math.floor(args.payment / (nominal_interest * math.pow(1 + nominal_interest, args.periods) / (math.pow(1 + nominal_interest, args.periods) - 1)))
        print(f"Your loan principal = {args.principal}!")
        print(f"Overpayment = {args.payment * args.periods - args.principal}")
    elif args.periods is None:
        nominal_interest = args.interest / (12 * 100)
        args.periods = math.ceil(math.log(args.payment / (args.payment - nominal_interest * args.principal), 1 + nominal_interest))
        years = args.periods // 12
        months = args.periods % 12
        if years == 0:
            print(f"It will take {months} months to repay this loan!")
        elif years == 1:
            if months == 0:
                print(f"It will take {years} year to repay this loan!")
            elif months == 1:
                print(f"It will take {years} year and {months} month to repay this loan!")
            else:
                print(f"It will take {years} year and {months} months to repay this loan!")
        else:
            if months == 0:
                print(f"It will take {years} years to repay this loan!")
            elif months == 1:
                print(f"It will take {years} years and {months} month to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")
        print(f"Overpayment = {args.payment * args.periods - args.principal}")
    elif args.payment is None:
        nominal_interest = args.interest / (12 * 100)
        args.payment = math.ceil(args.principal * nominal_interest * math.pow(1 + nominal_interest, args.periods) / (math.pow(1 + nominal_interest, args.periods) - 1))
        print(f"Your annuity payment = {args.payment}!")
        print(f"Overpayment = {args.payment * args.periods - args.principal}")



