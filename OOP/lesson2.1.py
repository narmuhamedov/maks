class French:
    def __init__(self, lang):
        self.lg = lang

    def greeting(self):
        return f'Bonjour'


class English:
    def __init__(self, lang):
        self.lg = lang

    def greeting(self):
        return f'Hello'


class Germany:
    def __init__(self, lang):
        self.lg = lang

    def greeting(self):
        return f'Hallo'


french = French(lang='French')
eng = English(lang='English')
gr = Germany(lang='Germany')
print(french.greeting(), eng.greeting(), gr.greeting())


# class BankAcount:
#     def __init__(self, login, password, secret_key):
#         self.lg = login
#         # self._ps = password
#         # self.__sk = secret_key
#
#     def balance(self, summary):
#         return f'Summary - {summary}'
#
#
#     def __str__(self):
#         return f'Login - {self.lg}\n' \
#                # f'Password - {self._ps}\n' \
#                # f'Secret_key - {self.__sk}'
#
# acc = BankAcount(login='qwerty', password=1234, secret_key='12;flsajkkjskadpaposjdqoo')
# #print(acc.__sk)
# print(acc.balance(1234))
# # print(acc._ps)
