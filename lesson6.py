movies = {
    "Mstiteli": {
        "John": 10,
        "Jack": 9
    },

    "Spider-Man": {},
}


def show():
    for name, rates in movies.items():
        print(f"\nФильм - {name}")
        if len(rates) == 0:
            print("Рейтинг еще не доступен.")
        else:
            print("Рейтинг:")
            for user, rate in rates.items():
                print(f"{user}: {rate}")


def add_movie(movie):
    if movie in movies.keys():
        print("Этот фильм уже добавлен!")
    else:
        movies.update({movie: dict()})


def add_rete(movie):
    if movie not in movies.keys():
        print("Такого фильма нет!")
    else:
        name = input("Введите имя человека: ")
        rate = int(input("Введите рейтинг: "))
        if rate < 0 or rate > 10:
            print("Оценка должна быть 1-10!")
        else:
            movies[movie].update({name: rate})
            print(f" Interstellar получил оценку: {name} оценено: {rate}")


def rate_view():
    for movie, rate in movies.items():
        rates = []
        for i in rate.values():
            rates.append(i)
        if len(rates) == 0:
            print(f"Рейтинг еще не доступен {movie}")
        else:
            print(f"{movie} оценка этого фильма {sum(rates) / len(rates)}")


while True:
    show()
    command = int(input("\nВведите команду(1 - добавить фильм, 2 - добавить оценку, 3 - просмотр оценок, 0 - конец программы): "))
    print('-'*50)
    if command == 0:
        print("Программа закончена!")
        break

    elif command == 1:
        movie = input("Напишите название фильма: ")
        add_movie(movie)
        print('Фильм успешно добавлен')
    elif command == 2:
        movie = input("Введите название фильма для добавления рейтинга: ")
        add_rete(movie)
    elif command == 3:
        rate_view()
    else:
        print("Такой команды нет!")








# contacts = [
#     {'name': 'Geektech', 'phone': '0507052018'},
#     {'name': 'Служба спасения', 'phone': '911'},
#     {'name': 'Пожарная служба', 'phone': '101'}
# ]
#
#
# def create(contacts_, name_, phone_):
#     for contact_ in contacts_:
#         # print(i)
#         for key_, value_ in contact_.items():
#             # print(f'{key} --> {value}')
#             if value_ == name_:
#                 # print(f'{key} --> {value}')
#                 print('That contact already exist')
#     new_contact = dict(name=name_, phone=phone_)
#     contacts_.append(new_contact)
#
#
# def edit(contacts_, name_):
#     for contact_ in contacts_:
#         print(contact_)
#         for key_, value_ in contact_.items():
#             # print(f'{key_} --> {value_}')
#             if value_ == name_:
#                 value_index = value_.index(value_)
#                 print(value_index)
#                 new_name = str(input('Enter new contact name --> '))
#                 contacts_.insert(value_index, new_name)
#                 print(contacts)
#                 break
#
#
# while True:
#     print('-' * 60 + '\n'
#                      'Commands:\n'
#                      '1. Show all contacts\n'
#                      '2. Add contact\n'
#                      '3. Edit contact\n'
#                      '4. Delete contact\n'
#                      '5. Exit\n' + '-' * 60)
#     command = int(input('Select command --> '))
#     if command == 1:
#         for contact in contacts:
#             for key, value in contact.items():
#                 print(f'{key}: {value}')
#     elif command == 2:
#         name_create = str(input('Enter contact name --> '))
#         phone_create = str(input('Enter contact phone --> '))
#         create(contacts, name_create, phone_create)
#         print('-' * 60)
#         for i in contacts:
#             print(i)
#         print('-' * 60)
#     elif command == 3:
#         name_edit = str(input('Enter contact name for edit --> '))
#         # phone_edit = str(input('Enter contact phone number for edit'))
#         edit(contacts, name_edit)
#     elif command == 5:
#         print('You leave the programm')
#         break
#     else:
#         print('This not a command')

# for i in contacts:
#     for key, value in i.items():
#         print(f'{key} --> {value}')







# while 1:
#     try:
#         first_number = float(input('Введите первое число: '))
#         operation = str(input('+ - / * '))
#         second_number = float(input('Введите второе число: '))
#     except:
#         print('Пишите пожалуйста только числа!!!')
#         continue
#
#     if operation == '+':
#         print(f'RESULT-{first_number+second_number}')
#
#     elif operation == '-':
#         print(f'RESULT-{first_number - second_number}')
#
#
#     elif operation == '*':
#         print(f'RESULT-{first_number * second_number}')
#
#
#     elif operation == '/':
#         print(f'RESULT-{first_number / second_number}')
#
#     else:
#         print('Что то пошло не так........')
#         break

# try:
#     a = 5
#     b = "4"
#     print(a+b)
#
# except:
#     print('Нельзя так делать!!!')


# words = ['apple', 'banana', 'red', 'qwerty', 'hello']
# a = list(filter(lambda x: len(x)>5, words))
# print(a)

# nums = [1, 2, 3, 4, 5, 6]
# a = list(filter(lambda x: x%2==0, nums))
# print(a)

# lst = ['word', 'python', 'apple']
# b = list(map(lambda x: x.upper(), lst))
# print(b)

# def upletter(lst):
#     for i in lst:
#         print(i.upper())
#
# upletter(lst)




# def plus(x, y):
#     return x+y
#
# print(plus(2,3))
#
# plusl = lambda x, y: x+y
# print(plusl(2, 3))
#


# a = [1, 2, 3, 4, 5]
# a5 = []
# def plus_each(lst, fn):
#     for i in lst:
#         a5.append(i+fn)
#
# plus_each(a, plus(2,3))
# print(a5)