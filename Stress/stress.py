with open('spam.txt') as file1:
    file2 = open('stress.txt', 'w')
    list1 = file1.readlines()

    for line in list1:
        line = line.strip()

        if line.isupper() and line.endswith('!!!') or 'help' in line or 'asap' in line or 'urgent' in line:
            file2.write(line + '\n')
        elif line.isupper() or line.endswith('!!!') or'HELP' in line or 'ASAP' in line or 'URGENT' in line:
            file2.write(line + '\n')

    print('Finished')


