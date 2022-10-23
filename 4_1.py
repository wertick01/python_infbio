import math

print('\n#4.1')

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

values = []
helper = []
with open('input.4.1.txt', 'r') as file:
    for line in file.readlines():
        helper.append(line.strip())
        rs = line.split(' ')
        if len(rs) == 3 and (is_number(rs[0]) and is_number(rs[1]) and is_number(rs[2])):
            values.append([float(i) for i in line.split(' ')])
        else:
            values.append(None)

def func(a, b, c):
    try:
        if a == 0 and b == 0 and c == 0:
            return 'Бесконечно много корней'
        
        D = b**2 - 4*a*c

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            return x1, x2
        elif D == 0:
            x = -b / (2 * a)
            return x
        else:
            return 'Корней нет'
    except ZeroDivisionError:
        return 'Деление на нуль'

result = []

for line in values:
    if line != None:
        aa = func(line[0], line[1], line[2])
        result.append(aa)
    else:
        result.append('Некорректные данные')

with open('output.4.1.txt', 'w') as file:
    for i in range(len(helper)):
        suffix = ''
        if len(helper[i]) < 3:
            suffix = len(helper[i])*' '
        file.write(helper[i]+f'{suffix}\t-->\t'+str(result[i])+'\n')