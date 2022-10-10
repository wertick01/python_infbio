from random import randrange

generated = randrange(0, 101)
# To know the walue decomment next line
# print('Generated value is: ', generated)

count = 0

while True:
    users_value = int(input())
    count += 1
    if users_value == generated:
        print('Oh, Yes! Yes mthfckr, you win!!!\nyout value is -->', generated, '<-- and attempt is -->', count, ' <--')
        break

    elif users_value > generated:
        print('Oh, you are looser bc your value is bigger\n')

    else:
        print('Oh, you are looser bc your value is smaller\n')