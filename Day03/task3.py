# If the bmi is under 18.5 (not including), print out "underweight"

# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

# If the bmi is 25 (including) or over, print out "overweight"

weight = int(input("Enter your weight: "))
height = int(float(input("Enter your height: ")))

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if 18.5 > bmi:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")    