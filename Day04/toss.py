import random
toss = random.randint(1, 50)

# print(toss)
win = toss % 2
# print(win)
if win == 0:
    print("Heads")
else:
    print("Tails")

# #
# import random
# toss = random.randint(0, 1)
# if toss == 0:
#     print("Heads")
# else:
#     print("Tails")
