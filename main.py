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
computer_choice = random.randint(0, 2)

user_choice = int(input("Please enter '0' for Rock, enter '1' for Paper, or enter '2' for Scissors.\n"))

if user_choice == '0':
    if computer_choice == 0:
        print(f"{rock}\n{rock}\nIt's a tie.")
    elif computer_choice == 1:
        print(f"{rock}\n{paper}\nYou lose. Paper beats rock.")
    elif computer_choice == 2:
        print(f"{rock}\n{scissors}\nYou win! Rock beats scissors.")
elif user_choice == '1':
    if computer_choice == 0:
        print(f"{paper}\n{rock}\nYou win! Paper beats rock.")
    elif computer_choice == 1:
        print(f"{paper}\n{paper}\nIt's a tie.")
    elif computer_choice == 2:
        print(f"{paper}\n{scissors}\nYou lose. Scissors beats paper.")
elif user_choice == '2':
    if computer_choice == 0:
        print(f"{scissors}\n{rock}\nYou lose. Rock beats scissors.")
    elif computer_choice == 1:
        print(f"{scissors}\n{paper}\nYou win! Scissors beats paper.")
    elif computer_choice == 2:
        print(f"{scissors}\n{scissors}\nIt's a tie.")
else:
    print("Please enter '0', '1', or '2' for your choice.")
