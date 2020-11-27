with open('rock.txt') as file1:
    list1 = file1.readlines()
    print(len(list1))
    i = 1
    for line in list1:
        print(f'B {i} строке - {len(line)} символов')
        i += 1


