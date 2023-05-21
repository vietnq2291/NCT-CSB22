month = int(input("Input a month: "))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("This month has 31 days")
elif month == 2:
    print("This month has 28 days")
else:
    print("This month has 30 days")