print('# 1.1')

var1, var2, var3 = int(input('a: ')), int(input('b: ')), int(input('c: '))

def func(x, a, b, c):
    return a*x*x + b*x +c

print("-->", func(3, var1, var2, var3), '\n')