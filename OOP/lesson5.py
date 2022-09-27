# Магические методы
class Cinema:
    def __init__(self, title, genre, time, release, rating, price):
        self.title = title
        self.genre = genre
        self.time = time
        self.release = release
        self.rating = rating
        self.price = price

    def title_method(self):
        return f'{self.title}'

    def __str__(self):
        return f'Movie title - {self.title}\n' \
               f'Genre - {self.genre}\n' \
               f'Running time - {self.time} minutes\n' \
               f'Release date - {self.release}\n' \
               f'Movie rating - {self.rating}%\n' \
               f'Ticket price - {self.price}$'


class Menu:
    def __init__(self, movies):
        self.movies = movies

    def movies_list(self):
        print('-' * 50)
        print('Movies:')
        for index, movie in enumerate(self.movies, start=1):
            print(f'{index}. {movie}')
        print('-' * 50)

    def movie_info(self, movie_index_):
        try:
            keys_list = list(self.movies)
            key_index = keys_list[movie_index_ - 1]
            print(self.movies.get(key_index))
        except IndexError:
            print('Movie under this index does not exist')


movies_dict = {
    'avengers_endgame':
        Cinema(
            title='Avengers: Endgame',
            genre='Action/Sci-fi',
            time=181,
            release='22.04.2019',
            rating=94,
            price=10
        ),

    'django_unchained':
        Cinema(
            title='Django Unchained',
            genre='Western/Action',
            time=165,
            release='11.12.2012',
            rating=93,
            price=10
        ),

    'interstellar':
        Cinema(
            title='Interstellar',
            genre='Sci-fi/Adventure',
            time=169,
            release='26.10.2014',
            rating=93,
            price=8
        ),

    'the_batman':
        Cinema(
            title='The Batman',
            genre='Action/Adventure',
            time=176,
            release='01.03.2022',
            rating=83,
            price=9
        ),

    'tenet':
        Cinema(
            title='Tenet',
            genre='Action/Sci-fi',
            time=150,
            release='03.09.2020',
            rating=81,
            price=11
        )

}

movies_dict.update({
    'american_psycho':
        Cinema(
            title='American Psycho',
            genre='Horror/Thriller',
            time=102,
            release='14.04.2000',
            rating=90,
            price=12
        )}
)


while True:
    menu = Menu()
    menu.movies_list()
    movie_index = int(input('Enter movie index\n--> '))
    menu.movie_info(movie_index)
