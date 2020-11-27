def write(filename, mode):
    if mode == 'read':
        file1 = open(filename)
        print(file1.read())
    elif mode == 'write':
        file1 = open(filename, 'w')
        text = input('Input text: ')
        file1.write(text)
write('spam.txt', 'write')
