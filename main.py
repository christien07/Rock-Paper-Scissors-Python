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

user_choice = input("Please enter '0' for Rock, enter '1' for Paper, or enter '2' for Scissors.\n")

if user_choice == '0':
    if computer_choice == 0:
        print(f"{rock}\n{rock}\nIt's a tie.")
    elif computer_choice == 1:
        print(f"{rock}\n{paper}\nYou lose. Paper beats rock.")
    elif computer_choice == 2:
        print(f"{rock}\n{scissors}\nYou win! Rock beats scissors.")
elif user_choice == '1':
    # Do something ...
    print("0")
elif user_choice == '2':
    # Do something else ...
    print("0")
else:
    print("Please enter '0', '1', or '2' for your choice.")