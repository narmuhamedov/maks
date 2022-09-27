import random
global user

secret = random.randint(1, 100)
count = 0

range_5 = []
range_10 = []
range_100 = []

for i in range(1, 6):
    i5_plus = secret + i
    range_5.append(i5_plus)
    i5_minus = secret - i
    range_5.append(i5_minus)

for j in range(6,11):
    i10_plus = secret + j
    range_10.append(i10_plus)
    i10_minus = secret - j
    range_10.append(i10_minus)

for k in range(-1,100):
    k += 1
    range_100.append(k)

while 1:
    count += 1
    try:
        print('')
        user = int(input('Программа загадало число от 0 до {}.\n'
                         'Ваше число: '.format(len(range_100) - 1)))
        if user in range_100:
            if user == secret:
                print('\nВы ввели число: {} \n'
                        'Программа загадало число = {} \n'
                        'Вы угадали, ура!\n'.format(user,secret))
                print('>>> Неверные попытки: {}'.format(count - 1))
                break
            elif user in range_5:
                print('Очень близко')
            elif user in range_10:
                print('Близко')
            elif user < secret:
                print('Ваше число меньше "<"')
            elif user > secret:
                print('Ваше число больше ">"')
            else:
                print('Не угадали')
        else:
            print('Вводите только числа от 1 до {}'.format(len(range_100) - 1))

    except ValueError:
        print('Вводите только целые числа')


# import random
# import time
# rnd = random.randint(0,100)
# atempts = 0
# start = time.time()
# while 1:
#     try:
#         numbers = int(input('Введите целое число от 0 до 100 '))
#         atempts +=1
#         if numbers<0 or numbers>100:
#             print("вводите пожалуйста от 0 до 100 ")
#             print('-'*50)
#             continue
#     except:
#         print('вводите пожалуйста только числа ')
#         continue
#     if rnd == numbers:
#         print(f'Поздравляю вы выйграли! ваши поптыки {atempts} \n ваше время {round(time.time() - start)} секунд')
#         break
#     if numbers>rnd:
#         print('Загаданное число меньше')
#         print('-' * 50)
#     if numbers<rnd:
#         print('Загаданное число больше')
#         print('-' * 50)
#     if abs(numbers - rnd) <= 5:
#         print('Очень близко')
#         print('-' * 50)
#     elif abs(numbers - rnd) <= 10:
#         print('Близко')
#         print('-' * 50)
#     else:
#         print('вы очень далеко от числа ')
#         print('-' * 50)
#
# # Написать программу, которая загадывает одно случайное число от 1 до 100, а пользователь старается угадать.
# # Программа должна запрашивать у пользователя целое число, в бесконечном цикле, пока оно не будет отгадано.
# # Исключать ошибки ввода букв и ограничить ввод числа больше 100 и меньше 0, подсказывать пользователю корректный ввод для каждого отдельного случая.
# # Если пользователь отгадал число, вывести на экран количество потраченных попыток и секунд затем выйти из программы.
# # Программа должна подсказывать знаком “>” или “<” и “очень близко” при радиусе 5 и “близко” при 10.
#
