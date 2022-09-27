class Junior_Dev:
    def __init__(self, laptop, salary, prog_lang):
        self.lp = laptop
        self.sl = salary
        self.pr_lg = prog_lang

    def copy_paste(self, resourse):
        return f'can copy paste from - {resourse}'


    def __str__(self):
        return f'Ноутбук - {self.lp}\n' \
               f'ЗП - {self.sl}$\n' \
               f'Языки Программирования - {self.pr_lg}'


proger = Junior_Dev(laptop=True, salary=550, prog_lang="Python")
print(proger.copy_paste("StackOverFlow"))
print(proger)

class Middle_Dev(Junior_Dev):
    def __init__(self, laptop, salary, prog_lang, expirience, responsibility):
        super().__init__(laptop, salary, prog_lang)
        self.exp = expirience
        self.rb = responsibility

    def interview(self, man_name):
        return f'Middle proger can take on a job - {man_name} '


    def __str__(self):
        return super(Middle_Dev, self).__str__()+f'\nОпыт - {self.exp}\n' \
                                                 f'Личные качества - {self.rb}'


print('-'*20)
midle_prog = Middle_Dev(laptop=True, salary=1000, prog_lang="Python , C++", expirience=2.5,
                        responsibility="Can be write good CODE")

print(midle_prog.copy_paste("StaStackOverFlow"))
print(midle_prog.copy_paste("Other IT RESOURSE"))
print(midle_prog.interview('Jack'))
print(midle_prog.interview('John'))
print(midle_prog)


class Senior_Dev(Middle_Dev):
    def __init__(self, laptop, salary, prog_lang, expirience, responsibility, team_lead):
        super().__init__(laptop, salary, prog_lang, expirience, responsibility)
        self.tm = team_lead

    def advanced_skill(self, lang):
        if lang == 'Python':
            return 'You are good proger'
        elif lang == 'Java':
            return 'You are bad proger'
        else:
            return 'Who are you man?'

    def __str__(self):
        return super(Senior_Dev, self).__str__()+f'\n Тим Лидер - {self.tm}'


print('-'*20)
senior_proger = Senior_Dev(laptop=True, salary=5000, prog_lang='python, php, c++,c#, ruby',expirience=12.5,
                           responsibility="Can be Director", team_lead=True)
print(senior_proger.copy_paste('Stack'))
print(senior_proger.interview('Elena'))
print(senior_proger.advanced_skill(input('какой язык учили? ').title()))
print(senior_proger)