 

#BT1: 
cNum = int(input("Number: "))
if cNum < 13: 
    print("This number is not larger than 13")
else: 
    print("This number is larger than 13")

#BT2: 
cNum2 = int(input("Number: "))
if cNum2 % 2 == 0: 
    print("This number is even")
else: 
    print("This number is not even")

#BT3:
cMonth = int(input("Month: "))
if cMonth > 0 and cMonth <= 12: 
    if cMonth == 1 or cMonth == 3 or cMonth == 5 or cMonth == 7 or cMonth == 8 or cMonth ==10 or cMonth == 12:
        print("This month has 31 days.")
    elif cMonth == 4 or cMonth == 6 or cMonth == 9 or cMonth == 11:
        print("This month has 30 days.")
    else: 
        print("This month has 28 (or 29) days.")