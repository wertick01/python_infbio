from curses.ascii import isdigit
import math
from re import X

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

values = []
with open('input.4.1.txt', 'r') as file:
    for line in file.readlines():
        rs = line.split(' ')
        if len(rs) == 3:
            if is_number(rs[0]) and is_number(rs[1]) and is_number(rs[2]):
                values.append([float(i) for i in line.split(' ')])
print(values)

def func(a, b, c):
    D = b**2 - 4*a*c
    try:
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            return x1, x2
        elif D == 0:
            x = -b / (2 * a)
            return x
        else:
            return None
    except ZeroDivisionError:
        return None

for line in values:
    print(func(line[0], line[1], line[2]))