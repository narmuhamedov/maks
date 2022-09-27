# #структура данных списки list кортежи tuple
# nominal = (1,3,5,10,20,50,100,200,500,"1k","2k","5k","5k")
# # print(nominal.count("5k"))
# # print(nominal.index(1))
# print(type(nominal))
#
# nominal = list(nominal)
# nominal.append(1233421)
# nominal = tuple(nominal)
#
# print(nominal)
#

a = 'python'
a = list(a)

a.reverse()
print(a)






# data_type = ['hello', 123, True, 'world', 12.3, False, 44.33333]
# name = "Radomir"
# name = list(name)
# name.reverse()
# print(name)

# data_type2 = [12,33,12,34,12]
# data_type.pop(2)
# da = list()
# da.append(data_type.pop(2))
# print(
#     da
# )

# data_type2.append(data_type.pop(1))
# print(data_type2)

#метод расширения
# data_type.extend(data_type2)


# data_type.clear()

# numbers = [12,33,22,12,33.33,4,1,23,4,5,21,3,13,1]
# numbers.sort()
# print(numbers)

# for i in data_type:
#     if i == "hello" or i == "print":
#         print(i)


#изменять 1 метод
# data_type[0]= "Name"

#удалять2(метода)
# data_type.remove(False)
# del data_type[-1]

#добавлять 2(метода)
# data_type.append("Maksim")
# data_type.append("KSLA")
#
# data_type.insert(1,4)



#
# print(data_type)

















# random_number = int(input("введите число от 1 до 100? "))
# left = 0
# right = 101
# attempts = 0
# while 1:
#     answer = (right+left)//2
#     attempts += 1
#     print(f'колличество попыток-{attempts}')
#     print(f'ответ компьютера {answer}')
#     if answer == random_number:
#         print(f'комп нашел ваше число!')
#         break
#     elif answer>random_number:
#         print('загаданное число меньше ')
#         right = answer
#     elif answer<random_number:
#         print('загаданное число больше ')
#         left = answer
#     print(f'минимальное колличество попыток-{attempts}')