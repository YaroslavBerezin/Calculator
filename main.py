#   Version 1.01

def calculate():
    x = input("What to do? Enter + / - / * / : / ** / CI (compound interest) / SR (square root) : ")
    if x in "+, -, *, /, **":
        a = int(input("Enter the 1st number: "))
        b = int(input("Enter the 2nd number: "))
        if x == '+':
            print(a + b)
        elif x == '-':
            print(a - b)
        elif x == '*':
            print(a * b)
        elif x == ':':
            print(a / b)
        elif x == '**':
            print(a ** b)
    elif x == 'CI' or x == 'ci':
        p = float(input('Enter the starting investment amount: '))
        r = float(input('Enter the annual interest rate (%): ')) / 100
        n = float(input('Enter the number of times that interest is compounded per unit time: '))
        t = float(input('Enter the time the money is invested or borrowed for (years): '))
        a = p * ((1 + r / n) ** (n * t))
        if a % 1 == 0:
            print(int(a))
        else:
            print(a)
    elif x == 'SR' or x == 'sr':
        a = int(input('Enter a number: '))
        if (a ** 0.5) % 1 == 0:
            print(int(a ** 0.5))
        else:
            print(a ** 0.5)
    else:
        print("Sorry, I can't that.")


calculate()
input()
