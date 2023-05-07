# Bài 1
n1 = float(input("Number 1: "))
n2 = float(input("Number 2: "))
n3 = float(input("Number 3: "))
if n1 > n2 and n1 > n3:
    print("The largest number:",n1)
elif n2 > n3 and n2 > n1:
    print("The largest number:",n2)
elif n3 > n1 and n3 > n2:
    print("The largest number:",n3)
else:
    print("Don't have")

# Bài 2
year = int(input("Enter year: "))
if year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Bài 3
import math
a = float(input('a'))
b = float(input('b'))
c = float(input('c'))
delta = b**2-4*a*c

if delta < 0:
    print('no solution')
elif delta == 0:
    print('x1=x2=', -b/2*a)
elif delta > 0:
    x1 = -b+math.sqrt(delta)/2*a
    x2 = -b-math.sqrt(delta)/2*a
    print(x1,x2)