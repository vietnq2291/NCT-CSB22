BÀI 1
a = int (input("Input number: "))
if a % 2 == 0:
    print(a, "is even")
else:
    print(a, "is odd")

BÀI 2
a = float (input("Input number: "))
if a == int(a): 
    print (a,"is an integer")
else: print(a,"is not an integer")

BÀI 3
a = (input("Input character: "))
if a .isdigit():
    print(f"'{a}' is a digit")
else:
    print(f"'{a}' is not a digit")

BÀI 4
a = int (input("Input number: "))
if a % 3 == 0 and a % 5 == 0:
    print (a, "is divisible by 3 and 5")
if a % 3 == 0 and a  % 5 != 0:
    print (a, "is divisible by 3")
if a  % 3 != 0 and a % 5 == 0:
    print (a, "is divisible by 5")
else: 
    print (a, "is not divisible by 3 or 5") 

BÀI 5
print("Welcome to The Ultimate Sercurity System")
a = input("Username: ")
b = input("Password: ")
if a == "admin" and b == "123456":
    print("You are logged in, admin.")
else:
    print("Wrong username or password.")

BÀI 6
a = float (input("Insert length 1: "))
b = float (input("Insert length 2: "))
c = float (input("Insert length 3: "))
if a + b > c and b + c > a and c + a > b:
    print ("The 3 line segments can form a triangle")
else:
    print ("The 3 line segments cannot form a triangle")

BÀI 7
import turtle
t = turtle.Turtle()
a = float (input("Insert length 1: "))
b = float (input("Insert length 2: "))
c = float (input("Insert length 3: "))
if a + b < c and b + c < a and a + c < b:
    print ("")    
elif a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*c == a*a:
    print ("The 3 line segments can form a right triangle")
elif a == b == c:
    print ("The 3 line segments can form an equilateral triangle")
    t.forward (a/2)
    t.left (120)
    t.forward (a)
    t.left (120)
    t.forward (a)
    t.left (120)
    t.forward (a/2)
else:
    print ("The 3 line segments can form a triangle") 
