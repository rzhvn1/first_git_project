n = int(input('Please input any number you want: '))

def sum_of_square(n:int):
    result = (n * (n + 1) * (2 * n + 1))/6

    print(result)

sum_of_square(n)
