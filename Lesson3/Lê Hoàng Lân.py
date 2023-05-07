#Bài 1
a = float(input("Number 1: "))
b = float(input("Number 2: "))
c = float(input("Number 3: "))

if a > b  and a > c:
    print(f"The largest number is {a}")
elif b > a  and b > c:
    print(f"The largest number is {b}")
elif c > b  and c > a:
    print(f"The largest number is {c}")

#Bài 2
a = float(input())
if a % 400 ==0:
    print("is a leap year" , a)
elif a % 4 ==0 and a %100 !=0:
    print("is a leap year", a)
else:
    print( "is not a leap year", a)
    
#Bài 3
a = float(input("Number 1: "))
b = float(input("Number 2: "))
c = float(input("Number 3: "))
if a < 0:
    print("This equation has no solution")
delta = b**2 - 4*a*c
if delta == 0:
    print (f(root = {-b/2*a}))
x1= (-b + delta**(1/2))/(2*a)
x2= (-b - delta**(1/2))/(2*a)
print("Solution:")
print(x1)
print(x2)
