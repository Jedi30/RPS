print("")
import sys
import random

playerchoice = input("Choose number : \n1. For Rock, \n2. For Paper, \n3/ For Scissor\n\n")

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, 3")

computerchoice = random.choice('123')    

computer = random.choice("123")

print("You chose :" + playerchoice + ".")
print("Python chose : " + computerchoice + '.')
print('')

if player == 1 and computer == 3:
    print('You win!')
elif player == 2 and computer == 1:
    print("You Win!")
elif player == 3 and computer == 2:
    print("You win!")
elif player == computer:
    ("Tie Game")

else :
    print("Python Win!")
