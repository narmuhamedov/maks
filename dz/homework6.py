# Создать список ten, состоящий из целых чисел от одного до десяти
ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Список ten: {ten}')
# Создать список evens, который состоит из четных чисел списка ten
evens = list(filter(lambda x: x % 2 == 0, ten))
print(f'Четные числа {evens}')
# Вывести на экран список возведенных в квадрат чисел от списка evens.
step = list(map(lambda x: x ** 2, evens))
print(f'Возведенные в квадрат числа: {step}')

# Создать функцию для вывода объекта списка по указанному индексу.
def index(lst=ten):
    while True:
        b = input("Введите индекс, или exit для выхода:")
        if b != "exit":
            try:
                print(lst[int(b)])
            except:
                print('введите индекс от 0 до', len(lst) - 1)
                continue
        else:
            break


index()

