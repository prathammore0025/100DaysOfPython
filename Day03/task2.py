print("Welcome to rollercloster project!\n")
hight = int(input("What is your hight? "))
if hight >= 120:
    print("Your allow to ride..")
    age = int(input("How old are you? "))
    if age <= 12:
        bill = 5
        print("Pay $5.")
    elif age <= 18:
        bill = 12
        print("Pay $12.")
    else:
        bill = 20
        print("Pay $20.")
    photo = input("do you want a photo? y for yes n for no: ")
    if photo == "y":
        bill += 3
        print(f"your total bill is ${bill}")
else:
    print("Not Allow")