#функции
univer = []
kolledj = []
army = []
married = []

abiturients = [
    {"name": "Maksim", "ORT":110, 'gender':"male"},
    {"name": "Nina", "ORT":150, 'gender':"female"},
    {"name": "Kanat", "ORT":90, 'gender':"male"},
    {"name": "Egor", "ORT":12, 'gender':"male"},
    {"name": "Angelina", "ORT":10, 'gender':"female"}
]

def all_abit(lst):
    for i in lst:
        for key, value in i.items():
            print(f'{key}-{value}')

def selection(lst, univer:list,kolledj:list, army:list, married:list):
    for i in lst:
        if i["ORT"]>=110:
            univer.append(i)

        elif i["ORT"]<=109 and i["ORT"]>=45:
            kolledj.append(i)

        elif i["ORT"]<45 and i["gender"]=="male":
            army.append(i)

        elif i["ORT"]<45 and i["gender"]=="female":
            married.append(i)

selection(abiturients,univer, kolledj, army, married)
print('-'*30)
print(f'V UNIVER - {univer}\n'
      f'V Kollegje - {kolledj}\n'
      f'V Army - {army}\n'
      f'Za Muj - {married}')

# def sum_(*args):
#     return sum(args)/len(args)
#
# print(sum_(1,3,4,5,3,3,2,2,1))

# def menu(**vasya):
#     return vasya
#
# monday = menu(breakfast = "Яйичница", lunch="Борщ", dinner="Чай")
# print(monday)


# def result(*args):
#     return args
#
# a = result(1,3,4,5,6,7,2,4,5,6,7,3,2,2,1,1,1,3,4,5,5)
# b = result("Egor", "Andrew")
# print(b,a)
# print(type(a))
#



# def about_my_self(name,hobby, age, height, laptop):
#     return f'My name is {name}\n' \
#            f'My hobby is {hobby}\n' \
#            f"I'm {age} Y.O.\n" \
#            f"My height is {height} sm\n" \
#            f"I have laptop {laptop}"
#
# about = about_my_self(input("name? "), input("hobby? ")
#                       , input("age"), input("height? "), input("Laptop"))
# print(f'My Biograpfy\n'
#       f'{about}')



# def summa(a,b,c):
#     return a+b+c/3
#
# print(summa(1,3,4))


# def summa(a,b=3):
#     print(
#         a+b
#     )
#
# summa(1,45)


# def greeting(name):
#     print(f'Hello- {name}')
#
# greeting("Maksim")
# greeting("Danil")
# greeting("Imran")
# greeting("Kanykei")



# def square(a,b):
#     print(a*b)
#
# square(12,34)
# square(1,3)