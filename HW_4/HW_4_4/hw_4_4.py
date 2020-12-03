Limac = int(input('Please input the weight of Limac: '))
Bob = int(input('Please input the weight of Bob: '))

def Limac_and_Bob(a:int, b:int):
    if 1 <= a <= b <= 10:
        year = 0
        while a <= b:
            a = a * 3
            b = b * 2
            year += 1

    else:
        print('The weight of a and b should be in range (1 <= a <= b <= 10)')

    if year > 1:
        print(f'In {year} years the weight of Limac will be bigger than the weight of Bob')
    else:
        print(f'In {year} year the weight of Limac will be bigger than the weight of Bob')

Limac_and_Bob(Limac, Bob)


