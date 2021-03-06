#   Version 1.05
#   Fixed some bugs

from colorama import Fore, Back, Style, init

while 1 > 0:

    init()


    def calculate():
        x = input(
            'What to do? Enter + / - / * / : / ** / CI (compound interest) / SR (square root) / R (round number) : ')
        if x == "+" or x == "-" or x == "*" or x == ":" or x == "**":
            a = int(input('Enter the 1st number: '))
            b = int(input('Enter the 2nd number: '))
            if x == '+':
                return a + b
            elif x == '-':
                return a - b
            elif x == '*':
                return a * b
            elif x == ':':
                return a / b
            elif x == '**':
                return a ** b
        elif x == 'R' or x == 'r' or x == 'round':
            a = float(input('Enter the number: '))
            return round(a)
        elif x == 'CI' or x == 'ci':
            p = float(input('Enter the starting investment amount: '))
            r = float(input('Enter the annual interest rate (%): ')) / 100
            n = float(input('Enter the number of times that interest is compounded per unit time: '))
            t = float(input('Enter the time the money is invested or borrowed for (years): '))
            a = p * ((1 + r / n) ** (n * t))
            if a % 1 == 0:
                return int(a)
            else:
                return a
        elif x == 'SR' or x == 'sr':
            a = int(input('Enter a number: '))
            if (a ** 0.5) % 1 == 0:
                return int(a ** 0.5)
            else:
                return a ** 0.5
        else:
            return "Sorry, I can't that."


    print(Fore.GREEN, Style.BRIGHT)
    print(calculate())
