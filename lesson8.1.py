import random
import time
from random import randint, sample
import datetime

cash = 500
start = datetime.datetime.now()
while cash !=0:
    bet = int(input('Введите ставку\n'
                    f'доступно - {cash} '))

    comp = [randint(1, 6), randint(1, 6)]
    user = [randint(1, 6), randint(1, 6)]
    if sum(comp)>sum(user):
        cash-=bet
        print('Вы проиграли')
        with open('result.txt','a')as file:
            file.write(f'comp:{comp} - user: {user}'
                       f'You lose {sum(comp)}>{sum(user)}')
    elif sum(comp)<sum(user):
        cash+=bet
        print('Вы выйграли')
        with open('result.txt','a')as file:
            file.write(f'comp:{comp} - user: {user}\n'
                       f'You Win {sum(comp)}<{sum(user)}\n')

    else:
        print('Ничья')
        with open('result.txt', 'a')as file:
            file.write(f'comp:{comp} - user: {user}'
                       f'Draw {sum(comp)}=={sum(user)}')
n = datetime.datetime.now()-start
with open('result.txt', 'a')as file:
    file.write(f'\nОбщее время - {n}')



