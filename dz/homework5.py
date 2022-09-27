movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },

    "Spider-Man": {}
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