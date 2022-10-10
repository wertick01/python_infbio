from random import randrange

generated = randrange(0, 101)
print('Generated value is: ', generated)

users_value = int(input())
count = 0

while True:
    count += 1
    if users_value == generated:
        print('Oh, Yes! Yes mthfckr, you win!!!\nyout value is ', generated, ' and attempt is', count)
        break

    elif users_value > generated:
        print('Oh, you are looser bc your value is bigger')

    else:
        print('Oh, you are looser bc your value is smaller')