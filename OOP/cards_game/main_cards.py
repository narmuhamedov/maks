import random
import compare

class BlackJack:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.player = [random.choice(self.cards), random.choice(self.cards)]
        self.computer = [random.choice(self.cards), random.choice(self.cards)]
        self.die_or_win = [0, 1000, 0]

    def game(self):
        print('Choise Option\n'
              '1 Draw Card\n'
              '2 Draw Card only player\n'
              '3 Draw Card only computer\n'
              '4 Russian Rolette\n'
              f'Your cards{sum(self.player)}')
        choise = int(input('Your choise'))

        while 1:
            compare_1 = compare.CompareCards(player_list=self.player, computer_list=self.computer)
            if choise == 1:
                self.player.append(random.choice(self.cards))
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_result():
                    break
            elif choise == 2:
                self.player.append(random.choice(self.cards))
                if compare_1.compare_result():
                    break
            elif choise == 3:
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_result():
                    break
            elif choise == 4:
                self.computer.append(random.choice(self.die_or_win))
                self.player.append(random.choice(self.die_or_win))
                if compare_1.compare_result():
                    break
cards1 = BlackJack()
cards1.game()
