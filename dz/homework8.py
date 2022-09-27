from random import randint
import datetime

name = input("Напишите ваше полное имя: ")
attempts = 0
attempts = int(input("Введите количество попыток: "))
start = datetime.datetime.now()

while 1:
    num1 = randint(1, 9)
    num2 = randint(1, 9)
    action = num1 * num2
    print(f"Сколько будет {num1} x {num2} = ?", end=' ')
    result = int(input())
    print(f'Правильный ответ {action}')
    attempts -= 1

    with open('results1.txt', 'a' , encoding='utf-8') as file:
        if result == action:
            file.write(f"{num1} x {num2} = {result} ({action}) правильно\n")
        elif result != action:
            file.write(f"{num1} x {num2} = {result} ({action}) неправильно\n")

    if attempts == 0:
        datetime.datetime.now() -start
        with open('results1.txt', 'a', encoding='utf-8') as file:
            file.write(
                f"истраченные попытки: {attempts},"
                f"истраченное время: {(datetime.datetime.now() - start).seconds} секунд, "
                f"имя: {name}\n"
            )
        print("Все попытки были истрачены")
        print(f"Затраченное время: {datetime.datetime.now() - start} секунд")
        break