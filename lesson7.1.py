import random
import datetime
import time


# start = datetime.datetime.now()
# students = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(len(students))
# while len(students)!=0:
#     print(students.pop(students.index(random.choice(students))))
#     input('Next--> ')
#     print(students)
# end = datetime.datetime.now()-start
# print('Опрос завершен')
# print(f'Время программы: {end}')

def stopwach():
    start = 0
    while 1:
        print(start)
        time.sleep(1)
        start+=1
        if start == 60:
            print(start)
stopwach()