import random

while True:
     player = int(input("камень, 2-ножницы,3-бумага"))
     if player == 1:
         print("игрок выбрал камень")
     if player == 2:
         print("Игрок выбрал ножницы")
     if player == 3:
         print("Игрок выбрал бумагу")

     comp = random.randint(1, 3)
     if comp == 1:
         print("компьютер выбрал камень")
     if comp == 2:
         print("компьютер выбрал ножницы")
     if comp == 3:
         print("компьютер выбрал бумагу")
     win = 0
     if player == comp:
          win = 0
     if player == 1 and comp == 2:
          win = 1
     if player == 2 and comp == 3:
          win = 2
     if player == 3 and comp == 2:
          win = 2
     if player == 3 and comp == 2:
          win = 2
     if win ==0 :
          print("ничья")
     if win == 1 :
          print("победил игрок")
     if win == 2:
          print("победил компьютер")

