PHẦN 1
  Bài 1
  a =(input("First name: "))
b =(input("Last name: "))
print(f"Your full name is {a} {b}")
  
  Bài 2
  a =(input("Your input: "))
print(f"Capitalized: {a.upper()}")

Bài 3
  a =float(input("Input a number: "))
b=a**2
print("Squared input:",b)

Bài 4
import turtle
a =float(input("Input circle's radius: "))
turtle.circle(a, 360 )


Phần 2
Bài 1 
for i in range(3,13):
    print(i)
    
Bài 2
a =int(input("Your input: "))
b= a+1
for i in range(0,b):
    print(i)
    
Bài 3
a =int(input("Your input: "))
b= a+1
for i in range(1,b):
    if i%2==0:
        continue
    print(i)
Bài 4
import turtle
a = int(input("Input the number of edges: "))
if a > 2:
    if a == 3: 
        for x in range(a):
            turtle.forward(100)
            turtle.right(120)
    elif a > 3:
        b = ((a-2)*180)/a
        for x in range(a):
            turtle.forward(100)
            turtle.right(180-b)
else: print("Can not draw the polygon!!!")
  
  
  Phần 3
  Bài 1
  a = int (input("Input number: "))
if a > 13 == 0:
    print("This number is larger than 13")
else:
    print("This number is not larger than 13")

Bài 2
a = int (input("Input number: "))
if a % 2 == 0:
    print("This number is even")
else:
    print("This number is not even")
    
    
Bài 3
a = int (input("Input a month: "))
if a==2:
    print("This month has 28 days")
elif a <= 7 and a%2==1:
    print("This month has 31 days")
elif a > 7  and a%2==0:
    print("This month has 31 days")
else:
    print("This month has 30 days")
    
    
    
    
    
    
    
    
    Phần 4
Bài 1:
  print("== Registration ==")
a = input("Username: ")
b = input("Password: ")
c = input("Email: ")
if a == "admin" and b == "12345" and c == "abc@gmail.com":    
    print("Registered successfully.")
else:
    print("Wrong username or password.")
    
    
    
    
 Bài 2
print("== Registration ==")
a = input("Username: ")
b = input("Password: ")
if b != "12345":
    print("Passwords not match. Please input again.")
    b = input("Password: repeat: ")
c = input("Email: ")
if a == "admin" and b == "12345" and c == "abc@gmail.com":    
        print("Registered successfully.")
else:
    print("Can not registration.")
    
    
Bài 3:
  print("== Registration ==")
a = input("Username: ")
b = input("Password: ")
if b != "abc12345" and len(str(b)) != 8:
    print("Invalid password. Please input again.")
    b = input("Password repeat: ")
c = input("Email: ")
for digit in c:
    try: 
        digit != "@" or digit != "."
        print("Invalid email. Please input again.")
        c = input("Email repeat: ")
    except: digit == "@" or digit != "."
if a == "admin" and b == "abc12345" and c == "abc@gmail.com":    
        print("Registered successfully.")
else:
    print("Can not registration.")
    
    
    
Phần 5


import random
s=0
while True:
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    dau = random.randint(1,4)
    if dau == 1: 
        c = a-b
        checker = random.randint(0,1)
        if checker == 1:
            print(f"{a} - {b} = {c}")
            g = input("1 for True, 0 for False: ")
            if g == "1": 
                s=s+1
                print(f"Your Score: {s}")
            else: 
                print("== GAME OVER ==")
                print(f"Your total score is {s}")
                break
        elif checker == 0:
            c = c + 24
            print(f"{a} - {b} = {c}")
            g = input("1 for True, 0 for False: ")
            if g == "0": 
                s=s+1
                print(f"Your Score: {s}")
            else: 
                print("== GAME OVER ==")
                print(f"Your total score is {s}")
                break
    elif dau == 2: 
        c = a+b
        checker = random.randint(0,1)
        if checker == 1:
            print(f"{a} + {b} = {c}")
            g = input("1 for True, 0 for False: ")
            if g == "1": 
                s=s+1
                print(f"Your Score: {s}")
            else: 
                print("== GAME OVER ==")
                print(f"Your total score is {s}")
                break
        elif checker == 0:
            c = c + 24
            print(f"{a} + {b} = {c}")
            g = input("1 for True, 0 for False: ")
            if g == "0": 
                s=s+1
                print(f"Your Score: {s}")
            else: 
                print("== GAME OVER ==")
                print(f"Your total score is {s}")
                break
    elif dau == 3: 
        c = a*b
        checker = random.randint(0,1)
        if checker == 1:
            print(f"{a} * {b} = {c}")
            g = input("1 for True, 0 for False: ")
            if g == "1": 
                s=s+1
                print(f"Your Score: {s}")
            else: 
                print("== GAME OVER ==")
                print(f"Your total score is {s}")
                break
        elif checker == 0:
            c = c + 24
            print(f"{a} - {b} = {c}")
            g = input("1 for True, 0 for False: ")
            if g == "0": 
                s=s+1
                print(f"Your Score: {s}")
            else: 
                print("== GAME OVER ==")
                print(f"Your total score is {s}")
                break
    elif dau == 4: 
        c = a/b
        checker = random.randint(0,1)
        if checker == 1:
            print(f"{a} / {b} = {c}")
            g = input("1 for True, 0 for False: ")
            if g == "1": 
                s=s+1
                print(f"Your Score: {s}")
            else: 
                print("== GAME OVER ==")
                print(f"Your total score is {s}")
                break
        elif checker == 0:
            c = c + 24
            print(f"{a} / {b} = {c}")
            g = input("1 for True, 0 for False: ")
            if g == "0": 
                s=s+1
                print(f"Your Score: {s}")
            else: 
                print("== GAME OVER ==")
                print(f"Your total score is {s}")
                break




  
  
