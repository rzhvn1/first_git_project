file1 = open('spam.txt')
list1 = file1.readlines()
print(list1)
file2 = open('spam-message.txt', 'w')

for line in list1:
    if 'sales' in line or 'back to work' in line or 'help' in line or 'sos' in line:
        file2.write(line)
