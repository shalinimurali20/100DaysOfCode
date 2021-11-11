import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors  "))

# if choice==0:
#     print(rock)
# elif choice==1:
#     print(paper)
# else:
#     print(scissors)
if(choice>=3 or choice<0):
  print("Invalid Choice, you are eliminated")
else:
  print("You chose")
  game = [rock, paper, scissors]
  print(game[choice])

  print("Computer chose")

  choice_by_computer = random.randint(0,2)
  # if choice_by_computer==0:
  #     print(rock)
  # elif choice_by_computer==1:
  #     print(paper)
  # else:
  #     print(scissors)

  game = [rock, paper, scissors]
  print(game[choice_by_computer])

  if(choice == choice_by_computer):
      print("Match Draw")
  elif(choice_by_computer > choice):
      print("You lose")
  elif(choice > choice_by_computer):
      print("You won")
