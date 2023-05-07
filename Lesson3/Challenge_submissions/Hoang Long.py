Bai 1 :
a = int(input('number a:'))
b = int(input('number b: '))
c = int(input('number c: '))

largest = 0

if a > b and a > c :
    largest = a
elif b > c :
    largest = b
else :
    largest = c

print(largest, "is the largest of three numbers.")

Bai 2:
year = int(input("Enter the year: "))  
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))

Bai 3:
from math import*
a = float(input('a'))
b = float(input('b'))
c = float(input('c'))
delta = b**2-4*a*c

if delta < 0:
    print('no solution')
if delta == 0:
    print('x1=x2=', -b/2*a)
if delta >0:
    x1 = -b+sqrt(delta)/2*a
    x2 = -b-sqrt(delta)/2*a
    print(x1,x2)