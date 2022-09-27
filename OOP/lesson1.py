class Old_Phone:
    def __init__(self, model, wifi, bluetooth, camera, color, cpu):
        self.m = model
        self.wf = wifi
        self.bth = bluetooth
        self.c = camera
        self.clr = color
        self.cpu = cpu

    def call_parents(self, name_mother, name_father):
        return f'I can call my mother - {name_mother}\n' \
               f'I can call my father - {name_father}'


    def __str__(self):
        return f'Модель - {self.m}\n' \
               f'WIFI - {self.wf}\n' \
               f'Bluetooth - {self.bth}\n' \
               f'Camera - {self.c}\n' \
               f'Color - {self.clr}' \
               f'CPU - {self.cpu}HZ'

call_1 = Old_Phone(model='Motorolla', wifi=False, bluetooth=False, camera=False, color='black', cpu=1.0)
print(call_1.call_parents('Olga', "Tolik"))
print(call_1)

class Modern_Phone(Old_Phone):
    def __init__(self, model, wifi, bluetooth, camera, color, cpu, GPS, cabel_battery):
        super().__init__(model, wifi, bluetooth, camera, color, cpu)
        self.GPS = GPS
        self.c_b = cabel_battery

    def airpods(self, listen_music):
        return f'I have - {self.m} and I can {listen_music} in my phone'


    def __str__(self):
        return super(Modern_Phone, self).__str__()+f'\nGPS - {self.GPS}\n' \
                                                   f'cabel_battery - {self.c_b}'

phone1 = Modern_Phone(model='Iphone13', wifi=True, bluetooth=True, camera=True,
                      color='white',cpu=2.0, GPS=True, cabel_battery='Беспроводной')

print('-'*20)
print(phone1)
print(phone1.call_parents('Veronika', "Alex"))
print(phone1.airpods('aipods pro'))

# class Car:
#     def __init__(self, title, wheels, color, number, volume, person, cost):
#         self.title = title
#         self.wheels = wheels
#         self.color = color
#         self.number = number
#         self.volume = volume
#         self.person = person
#         self.cost = cost
#
#     def tunnig_auto(self, cost_tunning_auto):
#         return f'Общая цена за тюннинг будет равно - {self.cost + cost_tunning_auto}$'
#
#
#
#
#     def __str__(self):
#         return f'Название авто - {self.title}\n' \
#                f'Радиус колес - {self.wheels}\n' \
#                f'Цвет авто - {self.color}\n' \
#                f'Номер авто - {self.number}\n' \
#                f'Объем двигателя - {self.volume}\n' \
#                f'Колличество владельцев - {self.person} человека\n' \
#                f'Цена - {self.cost}$'
#
# car1 = Car(title="Фольцваген", wheels="195/65/r15", color='черный', number='881ach',
#            volume=1.6,person=3, cost=5000)
# print(car1)
# print(car1.tunnig_auto(5000))
# print('-'*20)
#
# car2 = Car(title="Lexus", wheels='145/55/r16', color='синий', number='654aad', volume=3.0, person=2, cost=10000)
# print(car2)
# print(car2.tunnig_auto(6000))
