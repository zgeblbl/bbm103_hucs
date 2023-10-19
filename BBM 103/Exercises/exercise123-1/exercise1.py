year = int(input("Please enter a year:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES! It is a leap year.")
else:
    print("NO! It is not a leap year.")
