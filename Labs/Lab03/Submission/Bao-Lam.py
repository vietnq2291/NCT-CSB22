# Bài 1
n1 = int(input("Input number: "))
if n1 % 2 == 0:
    print(f"{n1} is even")
else:
    print(f"{n1} is odd")

# Bài 2
n2 = float(input("Input number: "))
if n2 // 1 == n2 / 1:
    print(f"{int(n2)} is an integer")
else:
    print(f"{n2} is not an integer")

# Bài 3
n3 = input("Input character: ")
try:
    if int(n3) / 1 == int(n3) * 1:
        print(f"{n3} is a digit")
except ValueError:
    print(f"{n3} is not a digit")

# Bài 4
n4 = int(input("Input number: "))
if n4 % 3 == 0 and n4 % 5 == 0:
    print(f"{n4} is divisible by 3 and 5")
elif n4 % 3 == 0 and n4 % 5 != 0:
    print(f"{n4} is divisible by 3")
elif n4 % 5 == 0 and n4 % 3 != 0:
    print(f"{n4} is divisible by 5")
else:
    print(f"{n4} is not divisible by 3 and 5")

# Bài 5
print("Welcome to The Ultimate Sercurity System")
u1 = "admin"
p1 = "12345"
u2 = input("Username: ")
p2 = input("Password: ")
if u2 == u1 and p2 == p2:
    print("You are logged in, admin")
else:
    print("Wrong username or password")

# Bài 6
l1 = int(input("Input length 1: "))
l2 = int(input("Input length 2: "))
l3 = int(input("Input length 3: "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("The 3 line segements can form a triangle")
else:
    print("The 3 line segements can not form a triangle")

# Bài 7
import turtle as t
l1 = int(input("Input length 1: "))
l2 = int(input("Input length 2: "))
l3 = int(input("Input length 3: "))
if l1 == l2 == l3:
    print("The 3 line segements can form a equilateral triangle")
elif l1**2 + l2**2 == l3**2 or l1**2 + l3**2 == l2**2 or l2**2 + l3**2 == l1**2:
    print("The 3 line segements can form a right triangle")
elif l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("The 3 line segements can form a triangle")
else:
    print("The 3 line segements can not form a triangle")