num1 = int(input("Choose a number: "))
num2 = int(input("Choose a second number: "))
sum = num1 + num2
print()
print("The sum of", num1, "and", num2, "is", sum)
print()
if sum > 10:
    print("Your sum is greater than 10")
elif sum < 10:
    print("You sum is less than 10")
elif sum == 10:
    print("Your sum is equal to 10")

# Kelly Beltran
# 03-04-24
# Program takes two inputs, adds them to get a sum, and determine is sum is greater than, less than, or equal two 10