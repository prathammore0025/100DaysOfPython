import random

put = int(input("Enter a number 0 for rock, 1 for paper, 2 scissor\n"))
option = ["rock", "paper", "scissor"]

if put >= 3 or put < 0:
    print("invalid input")
    exit()
user = option[put]
computer = random.choice(option)


if user == option[0] and computer == option[2]:
    print("Bravo you win!!!")
elif user == option[0] and computer == option[1]:
    print("Uff's You loss...") 
elif user == option[0] and computer == option[0]:
    print("match tied")
elif user == option[1] and computer == option[2]:
    print("Uff's You loss...")
elif user == option[1] and computer == option[1]:
    print("match tied") 
elif user == option[1] and computer == option[0]:
    print("Bravo you win!!!")
elif user == option[2] and computer == option[2]:
    print("Match tied")
elif user == option[2] and computer == option[1]:
    print("You win...") 
elif user == option[2] and computer == option[0]:
    print("uff's you loss")
else:
    print("invalid input")
print(user, '=', computer)