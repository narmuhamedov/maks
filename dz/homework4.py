countries = {
    'kg': {'red', 'yellow'},
    'ru': {'white', 'red', 'blue'},
    'us': {'blue', 'red', 'white'},
    'tr': {'red', 'white'},
    'it': {'green', 'white', 'red'},
    'uk': {'blue','yellow'},
    'abh':{'green','red','white'}
}
while 1:
    colors = str(input("Введите цвета: "))
    colors = colors.split()
    a = []
    # items  делает словарь  парный список
    for k, v in countries.items():
        domen = True
        for c in colors:
            if c not in v:
                domen = False
        if domen == True:
            a.append(k)

    if len(a)==0:
        print('Домена нет')
    else:
        for i in a:
            print(i)

    exit = str(input('Хотите продолжить? y/n '))
    if exit == 'y':
         continue
    else:
         break