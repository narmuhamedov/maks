guessNum = int(input("введите число от 0 до 100 : "))
left = 0
right = 101
attempts = 0
while True:
    answer = (right + left) // 2
    attempts += 1
    print(' попыток №', attempts)
    print('компьютер сказал ', answer)
    if answer == guessNum:
        print("правильно он нашел ")
        break
    elif answer > guessNum:
        right = answer
    elif answer < guessNum:
        left = answer
print('минимальное количество попыток ', attempts)







# Программа должна работать в бесконечном цикле с возможностью выхода
# Запрашивать у пользователя любое слово на латинице или кириллице
# Считывать строчные и прописные буквы
# Вывести общее количество букв в данном слове
# Вывести количество согласных и гласных букв
# Вывести процентное соотношение гласных и согласных букв до двух цифрами после точки
while 1:
      word = str(input('Введите слово: '))
      print('Колличество символов в слове',len(word))
      glasnye = 'АУОЫЭЯЮЁИЕауоыэяюёиеAEIOUaeiou'
      soglasnye = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщBCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
      g = 0
      s = 0
      for i in word:
            if i in glasnye:
                  g+=1
            elif i in soglasnye:
                  s+=1
            else:
                  print('Вводите только буквы')
      print('Гласные: ',g)
      print('Согласные: ', s)
      print('гласные/согласные', round(g*100/len(word),2),'%  /', round(s*100/len(word),2),'%')

      n = int(input('Желаете продолжить нажмите 1 или 0: '))
      if n == 1:
            continue
      else:
           break
