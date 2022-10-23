from dis import findlabels
import random
from random import randrange

print('\n#3.2')

def Printer(dct) -> dict:
    for key, value in dct.items():
        print(key)
        if type(value) == list:
            for i in value:
                print(i)
        else:
            print(value)

def MaxChecker(maxval, x):
    result = ''
    if len(x) > maxval:
        maxval, result = len(x), x
    return maxval, result

def MinChecker(minval, x):
    result = ''
    if len(x) < minval:
        minval, result = len(x), x
    return minval, result

def MaxLength(dct) -> dict:
    maxlenth = 0
    res, result = '', ''
    for key, value in dct.items():
        if type(value) == str:
            maxlenth, res = MaxChecker(maxlenth, value)
        if (type(value) == list):
            maxlenth, res = MaxChecker(maxlenth, ''.join(value))
        if res != '':
            result = res
    print('\nThe longest sequence is', result, 'with lenght',  maxlenth)
    return

def MinLength(dct) -> dict:
    maxlenth = 120
    res, result = '', ''
    for key, value in dct.items():
        if type(value) == str:
            maxlenth, res = MinChecker(maxlenth, value)
        if (type(value) == list):
            maxlenth, res = MinChecker(maxlenth, ''.join(value))
        if res != '':
            result = res
    print('The shortest sequence is', result, 'with lenght',  maxlenth)
    return

def MostGC(dct) -> dict:
    finalseq = ''

    result = {
        'A': 0,
        'T': 0,
        'C': 0,
        'G': 0,
    }

    for _, value in dct.items():
        if type(value) == list:
            value = ''.join(value)
        if value.count('G') + value.count('C') > result['G'] + result['C']:
            result['A'], result['T'], result['G'], result['C'] = value.count('A'), value.count('T'), value.count('G'), value.count('C')
            finalseq = value
    
    print('Sequense with most [GC] is', finalseq, '-->', result)
    return


n = int(input('Put here the count of sequences: '))
dct = dict()

for i in range(n):
    seq = ''.join([random.choice('ATGC') for i in range(randrange(0, 121))])
    if len(seq) > 60:
        seq = [seq[0:60], seq[60:]]
    dct['\n> Sequence'+str(i + 1)] = seq

Printer(dct)
MaxLength(dct)
MinLength(dct)
MostGC(dct)
