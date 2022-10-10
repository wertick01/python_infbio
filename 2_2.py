
input_value = int(input("Номер элемента ряда Фибоначчи: "))

def n_first_values(n):
    fib1 = fib2 = 1
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')
    return

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n_first_values(input_value)
print('\n', fibonacci(input_value), sep = '')