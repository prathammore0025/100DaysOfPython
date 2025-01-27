# day02 project

print("Welcome to the tip calculator")
bill = int(input("What was a total bill: "))
tip = int(input("How much tip you like to give? 10, 12 or 15: "))
people= int(input("How many people to split the bill? "))
total = (bill+(tip/100*bill))/people
print(round(total))