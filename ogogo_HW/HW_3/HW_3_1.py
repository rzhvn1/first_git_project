string = 'follow me please and so we can be friends'
if string.count('f') == 1:
    print(string.index('f'))
elif string.count('f') >= 2:
    print(string.index('f'), string.rindex('f'))
else:
    print('this string doesnt have f')


