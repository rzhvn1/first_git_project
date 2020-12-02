string = 'hehhhEhehehehehHHHHeeeeHHHehHHHeh'
# string = string.replace('h', 'H', string.count('h') - 1).replace('H', 'h',1)
# print(string)



string1 = string[:string.find('h') + 1]
string2 = string[string.rfind('h'):]
string3 = string[string.find('h') + 1:string.rfind('h')]
string3 = string3.replace('h', 'H')
print(string1)
print(string2)
print(string3)
print(string1 + string3 + string2)