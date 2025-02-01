print("Welcome to pizza shop...!")

size = input("What pizza size you want? S, M or L? ")
perr = input("Do you want pepperoni on pizza? Y or N? ")
chees = input("Do you want extra cheese? Y or N? ")

# if size == "S":
#     size = 15
# elif size == "M":
#     size = 18
# elif size == "L": 
#     size = 20 
# else:
#     size = 0

# if perr == "Y":
#     perr = 2
# elif perr == "N":
#     perr = 0
# else:
#     print("Enter An valid Option.")

# if chees == "Y":
#     chees = 3
# elif chees == "N":
#     chees = 0
# else:
#     print("Enter An valid Option.")

# bill = size + perr + chees
# print(f"Your Bill is {bill}")

#
bill =0
if size == "S":
    bill += 15
elif size == "M":
    bill += 18
elif size == "L": 
    bill += 20
else:
    print("Please insert a valid Option.")

# 
if perr == "Y":
    if perr == "S":
        bill += 2
    else:
        bill += 5

# 
if perr == "Y":
    if perr == "S":
        bill += 2
    else:
        bill += 5
print(f"Your Total Bill is ${bill}")