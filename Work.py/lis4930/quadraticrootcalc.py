# question 1: quadratic equation root calculator.

import math


def quadraticroots(a, b, c):
    # calculate discriminant
    discriminant = b ** 2 - 4 * a * c
    # plus minus sign
    fancysym = u"\u00B1"
    # calculates roots based off of discriminant
    if discriminant > 0:
        print(f"The roots are: {(-b + math.sqrt(discriminant)) / (2 * a)} , {(-b - math.sqrt(discriminant)) / (2 * a)}")
    elif discriminant == 0:
        print(f"The roots is: {(-b + math.sqrt(discriminant)) / (2 * a)}")
    else:
        rp = -b / (2 * a)
        ip = math.sqrt(abs(discriminant)) / (2 * a)
        print(f"The roots are: {rp} {fancysym} {ip}i")


quadraticroots(1, -5.86, 8.5408)
quadraticroots(1, -4, 4)
quadraticroots(1, 2, 5)


def incdenominator(x):
    if x > 0:
        y = range(1, 11)
        for n in y:
            print(x/n)


incdenominator(1)
