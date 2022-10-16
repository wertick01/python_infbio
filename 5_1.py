import numpy as np

N = int(input('Put the value here: '))

matrix = np.random.randint(0, 10, (N, N))

def func(matrix):
    rows = np.sum(matrix, 1)
    columns = np.sum(matrix[1:-1], 0)

    outside = rows[0]+rows[-1]+columns[0]+columns[-1]

    return outside, np.sum(matrix)-outside

print(func(matrix))