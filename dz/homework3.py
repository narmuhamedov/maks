data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
#Создать два пустых списка letters и numbers
letters = []
numbers = []
# Пройтись циклом for по кортежу data_tuple, добавить все строки в список letters, а всё остальное в numbers.
for i in data_tuple:
        if type(i)==str:
            letters.append(i)
        else:
            numbers.append(i)
print(letters)
print(numbers)
# Из списка numbers удалить число 6.13 и переместить True в конец списка letters, затем вставить число 2 между 3 и 1
numbers.remove(numbers[0])
print(numbers)
a = numbers.pop(0)
letters.append(a)
numbers.insert(1,2)
print(numbers)
# Отсортировать numbers, реверсировать letters и изменить пару букв в letters.
numbers.sort()
letters.reverse()
print(letters)
print(numbers)
letters[1]='G'
letters[7] = 'c'
print(letters)
# Преобразовать списки numbers и letters в кортежи
letters_a = tuple(letters)
numbers_a = tuple(numbers)
print(letters_a)
print(numbers_a)