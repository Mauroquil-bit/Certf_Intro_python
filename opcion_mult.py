"""
Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
> Max
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
> 1 
> 2
> 1
Your age is 22; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
> 3
0 !
1 !
2 !
3 !
Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.
> 4
Please, try again.
> 2
Congratulations, have a nice day!
"""

def greet(bot_name, birth_year):                       # opcion_mult.py
    print('Hello! My name is ' + bot_name + '.')       # 
    print('I was created in ' + birth_year + '.')      # 


def remind_name():                                      # opcion_mult.py
    print('Please, remind me your name.')               # 
    name = input()                                      # 
    print('What a great name you have, ' + name + '!')  #   


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():                                         
    print("Let's test your programming knowledge.") 
    # write your code here
    if input() == '2':
        print('Completed, have a nice day!')
        

    else:
        print('Please, try again.')
    
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
# ...
end()

# #############################################################################
#

