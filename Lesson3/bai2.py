a = float(input())
if a % 400 ==0:
    print("is a leap year" , a)
elif a % 4 ==0 and a %100 !=0:
    print("is a leap year", a)
else:
    print( "is not a leap year", a)