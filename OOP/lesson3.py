class Phone:
    def __init__(self, name, cost, color, memory, camera, cpu):
        self.n = name
        self.c = cost
        self.clr = color
        self.mr = memory
        self.cam = camera
        self.cpu = cpu

    def call_to_someone(self, number):
        return f'This phone calling this number - {number}'

    def __str__(self):
        return f'Title - {self.n}\n' \
               f'Cost - {self.c}$\n' \
               f'Color - {self.clr}\n' \
               f'Memory - {self.mr}GB\n' \
               f'Camera - {self.cam}MPX\n' \
               f'CPU - {self.cpu}'

class Iphone(Phone):
    def __init__(self, name, cost, color, memory, camera, cpu):
        super().__init__(name, cost, color, memory, camera, cpu)

    def info(self):
        if self.n == 'Iphone13':
            return f'Best camera at moment'
        elif self.n == 'Iphone5':
            return f'This is Legend'
        elif self.n == 'Iphone2':
            return f'This is old Phone'

    def __str__(self):
        return super(Iphone, self).__str__()
ip13 = Iphone(name='Iphone13', cost=800, color='black', memory=1024, camera=16, cpu=2.4 )
print(ip13.call_to_someone("0550321123"))
print(ip13.info())
print(ip13)
print('-'*20)
class Nokia(Phone):
    def __init__(self, name, cost, color, memory, camera, cpu):
        super().__init__(name, cost, color, memory, camera, cpu)

    def unstopalbe(self, object):
        return f'crashed - {object}'

    def __str__(self):
        return super(Nokia, self).__str__()

nokia3310 = Nokia(name='3310', cost=20, color='blue', memory=1, camera=0, cpu=1.0)
print(nokia3310.unstopalbe('floor'))
print(nokia3310)