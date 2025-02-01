print(''' 
   __o        __o         __o          __o           
 _- \\_<,      _- \\_<,      _`\\<,_       _ \\_
(*)`(*)....(*)/'(*).....(*)/ (*).....(_)/(_)
''')
print("Welcome to Treasure Island.Your mission is to find the treasure.")
choice1 = input('which side do you want to go? right or left?\n' ).lower()

if choice1 == "right":
    choice2 = input("which way are you taking water or land?\n").lower()
    if choice2 == "water":
        choice3 = input("which door you want open red or black?\n").lower()
        if choice3 == "red":
            print("You win!!!!")
        else:
            print("game over")
    else:
        print("you took the wrong way. game over")
else:
    print("Game over! you fall in hole.")