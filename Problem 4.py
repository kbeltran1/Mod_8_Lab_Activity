def isLeapYear(year):
    if (year % 400 == 0):
        return True
    elif(year % 4 == 0):
        return True
    else:
        return False
# Choose a year to check and enter below where 0 is
print(isLeapYear(0))

# Kelly Beltran
# 03-04-2024
# Program allow you to change year in print message to check if a year is or is not a leap year
# if yes true will print, if no false will print