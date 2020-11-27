# import random
# # def add(str1, str2):
# #     result = str1 + str2
# #     return result
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # def greetings(name:str):
# #     return f'Hello, {name}. U r welcome!'
# #
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # def get_types(var1, var2, var3):
# #     return type(var1), type(var2), type(var3)
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # def calculator(number1:int, number2:int, sign:str):
# #     if sign == '+':
# #         result = number1 + number2
# #         print(number1, ' + ', number2, ' = ', result)
# #     elif sign == '-':
# #         result = number1 - number2
# #         print(number1, ' - ', number2, ' = ', result)
# #     elif sign == '*':
# #         result = number1 * number2
# #         print(number1, ' * ', number2, ' = ', result)
# #     elif sign == '//':
# #         result = number1 // number2
# #         print(number1, ' // ', number2, ' = ', result)
# #     else:
# #         print('ERROR 404!!!')
# #
# # # num1 = int(input('Please input the first number: '))
# # # num2 = int(input('Please input the second number: '))
# # # sign = input('Please input the sign: ')
# # # calculator(num1, num2, sign)
# #
# #
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # x = int(input('Please input the number: '))
# # print(x // 100)
# # print(x // 10 % 10)
# # print(x % 100 % 10)
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def register(username, email, password, check_password):
#     if password == check_password:
#         if 8 < len(username) < 40:
#             if 8 < len(password) < 16:
#                 print('Registration complete succesfully!')
#             else:
#                 print('Password is too small')
#         else:
#             print('Username is too small!')
#     else:
#         print('Incorrect data!')
#
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# username1 = 'rzhvn'
# email = 'erzhanmuratov99@gmail.com'
# password1 = 'erjan02'
#
# def auth(user_input, password):
#     if username1 == user_input and password1 == password or user_input == email and password1 == password:
#         print('You are welcome!')
#     else:
#         print('Incorrect data!')
#
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def coord(x, y):
#     if x > 0:
#         if y > 0:
#             print('1')
#         else:
#             print('4')
#     elif y > 0:
#         if x < 0:
#             print('2')
#     elif x < 0 and y < 0:
#         print('3')
#     else:
#         print('0')
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # number = random.randint(1,10)
# # print(number)
# #
# # number1 = random.sample
# # number1.sort()
# # print(number1)
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # list1 = [1,2,3,4,5,6,7,8,9,10]
# # i = 0
# #
# # while i < len(list1):
# #     check = list1[i] % 2
# #     if check == 0:
# #         print(list1[i])
# #     i += 1
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # list1 = ['Rasul', 'Erzhan', 'Atay', 0, 0, 'Almaz', 0, 'Ulan', 0, 0, 'Erkin']
# # list2 = []
# # i = 0
# #
# # while i < len(list1):
# #     if list1[i] != 0:
# #         list2.append(list1[i])
# #     i += 1
# #
# #
# # print(list2)
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # username = 'superuser'
# # password = 'erjan02'
# #
# # rock_list = ['superuser', 12312, 'erjan02', 'ahdsjad']
# # i = 0
# # j = 0
# #
# # while i < len(rock_list):
# #     if rock_list[i] == username or rock_list[i] == password:
# #         print(rock_list[i])
# #     i += 1
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # list1 = [1,2,3,4,5,5,5,6,7,8,9,9,10]
# # list2 = []
# #
# # # i = 0
# # # while i < len(list1):
# # #     if list1[i] not in list2:
# # #         list2.append(list1[i])
# # #
# # #     i += 1
# # # i = 0
# # # while i < len(list1):
# # #     count_i = list1.count(list1[i])
# # #     if count_i == 1:
# # #         list2.append(list1[i])
# # #     i += 1
# # #
# # # print(list1)
# # # print(list2)
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # lst = [1, 2, 3, 4, 5, 77]
# # lst.insert(0, 1)
# # print(lst)
# #
#
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# # bd_username = 'testuser'
# # bd_password = 'testpassword'
#
# def auth(tries:int):
#     count = 0
#     while count < tries:
#         username = input('Please input your username: ')
#         password = input('Please input your password: ')
#         if username == bd_username and password == bd_password:
#             print('Welcome!')
#             break
#         else:
#             print('Incorrect data!')
#         count += 1
#
# # def register_to_bd(username, password,check_password):
# #     if password == check_password:
# #         file1 = open('database.txt', 'w')
# #         result = username + '\n' + password
# #         file1.write(result)
# #
# # file1 = open('database.txt')
# # list1 = file1.readlines()
# #
# # my_input = input('I want ')
# # if my_input in list1:
# #     print('In stock')
# # else:
# #     print('Not in stock')
#



# with open('database.txt') as file1:
#     ban = 'ban_word' + '\n'
#     check_ban = ''
#     streamer_words = file1.readlines()
#
#     i = 0
#     while i < len(streamer_words):
#         if streamer_words[i] == ban:
#             check_ban = streamer_words[i]
#             print(streamer_words[i], streamer_words.index(streamer_words[i]) + 1)
#
#         i += 1
#
#     if check_ban in streamer_words:
#         print('Found!')
#     else:
#         print('OK')


# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# list1 = [1,2,3,4,5,6]
#
# print(list1[1:4:2])