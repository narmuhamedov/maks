#Сеты (SET)
borsh = {'мясо', 'капуста',"свекла", "картошка","лук", "Сметана0"}
lagman = {'мясо', 'лапша',"специи", "редька","лук", "лаза", "уксус"}
#находит похожее значение
# print(lagman.intersection(borsh))
# print(lagman & borsh)
#
# #нахождение микс значений
# print(lagman.union(borsh))
# print(lagman | borsh)

#вывод не одинаковых значений
# print(lagman.symmetric_difference(borsh))
# print(lagman^borsh)



# list1 = [1,3,1,1,1,2,3,3,4,5,6,7,8,9]
# list1_set = set(list1)
# print(type(list1_set))
# print(list1_set)





#словари
# nominal = [1,3,5,10,20,50,100,200,500,'1k','2k','5k']
# person = ['nothing','nothing','nothing','nothing','Moldo','Datka','Satylganov','000',
#           'Osmonov','Karalaev','Balasagyn','P']
# banknotes = dict(zip(nominal,person))
# for i,j in banknotes.items():
#     print(f'{i}--{j}')




# auto = dict(brand = "BMW", model='e34',color='black',year=1997)
# auto.update(year=2000)
# auto.update(volume=3.0)
#
# auto2 = auto.copy()
# auto2.update(crash=True)
# print(f'dict2---{auto2}')






# print(auto.keys())
# print(auto.values())
# for i,j in auto.items():
#     print(i,"--",j)
# # print(auto.get("brand"))


# student = {
#     'name':"Radomir",
#     'age': 24,
#     1997: "cow year",
#     'height':1.84,
#     "edication": True,
#     'hobby': ['read books', 'play guitar'],
#     'tel nummer': ["05506770", "123456789"]
# }
# print(student['tel nummer'][1])
# #добавление
# student["auto"] = True
# #удаление
# del student[1997]
# #Измение
# student['age']=25
#
# for keys, values in student.items():
#     print(f'{keys}---{values}')
#
#
# print(student)
# print(type(student))