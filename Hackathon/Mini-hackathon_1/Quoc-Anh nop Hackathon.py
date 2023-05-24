# Part 1

# # Bài 1
# First = input ("First Name: ")
# Last = input ("Last Name: ")
# print ("Your full name is ",First, Last)

# # Bài 2 
# Input_lower = input ("Your input: ")
# print ("Capitalized: ",Input_lower.upper ())

# # Bài 3
# Input = float(input("Input a number: "))
# print ("Squared input: ",Input**2)

# # Bài 4
# from turtle import *
# Radius = input ("Input circle radius: ")
# turtle.circle (Radius/2)

# Part 2

# # Bài 1 
# print (list(range(3,13,1)))

# # Bài 2
# n = int(input("Input a number: "))
# print (list(range(0,n + 1)))

# # Bài 3
# n = int (input("Input a number: "))
# print (list(range(1,n+1,2)))

# # Bài 4 
# from turtle import *
# x = int(input ("Input number of edges: "))
# for y in range (3, x):
#  Turtle.forward (100)
#  Turtle.right (360 / x)
 
# # Part 3 
# # Bài 1 
# a = float (input("Input a number: "))
# if a > 13:
#     print ("This number is greater than 13")
# elif a <= 13:
#     print ("This number is not greater than 13")

# # Bài 2
# b = int(input("Input a number: "))
# if b % 2 == 0:
#     print ("This number is even")
# elif b % 2 != 0:
#     print ("This number is not even")

# Bài 3 
c = int (input("Input a month: "))
if c == 1 or c == 3 or c == 5 or c == 7 or c == 8 or c == 10 or c ==12:
    print ("This month has 31 days") 
elif c == 2:
    print ("This month has 28 or 29 days")
else:
    print ("This month has 30 days")

# Part 4 

# Bài 1
print ("==  Registration  ==")
d = input ("Username: ")
d_1 = input ("Password: ")
e = input ("Email: ")

print ("Registered successfully.")

# Bài 2 
print ("==  Registration  ==")
d = input ("Username: ")
d_1 = input ("Password: ")
d_2 = input ("Repeat password: ")
while d_1 != d_2:
    print ('Password not match. Please input again.')
    d_2 = input ("Repeat password: ")
e = input ("Email: ")
print ("Registered successfully.")

# Bài 3 
print ("==  Registration  ==")
d = input ("Username: ")
d_1 = input ("Password: ")
d_2 = input ("Repeat password: ")
while d_1 != d_2:
    print ('Password not match. Please input again.')
    d_2 = input ("Repeat password: ")
while len(d1) < 8:
    print ("Invalid Password. Please input again.")
    d_1 = input ("Password: ")
e = input ("Email: ")
for y in range (len(e)):
    if e[y] != "@":
        print ("Invalid email. Please input again.")
        e = input ("Email: ")
    elif e[y] != ".":
        print ("Invalid email. Please input again.")
        e = input ("Email: ")
print ("Registered successfully.")

# Part 5
from random import *
print ("== FREAKING MATH CONSOLE ==")
print ("Give correct answers to get scores.")
while True: 
    Math_Symbols = "+-*/"
    Symbols_Chosen = Math_Symbols [random.randint (0,3)]
    num1 = random.randint (0,100)
    num2 = random.randint (0,100)
    num3 = random.randint (0,10000)
    score = 0 
    if Symbols_Chosen == "+":
        Sum = num1 + num2 
        print (num1 + num2 ,"=", num3)
        Ans = input ("1 for True, 0 for False")
        if Sum == num3 and Ans == 1:
            score += 1 
            print ("Score:", score)
        if Sum != num3 and Ans == 1:
            break 
            score += 0
            print ("== GAME OVER ==")
            print (" Your total score is ",score)
        
        if Sum == num3 and Ans == 0:
            break 
            score += 0
            print ("== GAME OVER ==")
            print (" Your total score is ",score)
        if Sum != num3 and Ans == 0:
            score += 1
            print ("Score:", score)
    
    if Symbols_Chosen == "*":
        Product = num1 * num2 
        print (num1 * num2 ,"=", num3)
        Ans = input ("1 for True, 0 for False")
        if Sum == num3 and Ans == 1:
            score += 1 
            print ("Score:", score)
        if Sum != num3 and Ans == 1:
            break 
            score += 0
            print ("== GAME OVER ==")
            print (" Your total score is ",score)
        if Sum == num3 and Ans == 0:
            break 
            score += 0
            print ("== GAME OVER ==")
            print (" Your total score is ",score)
        if Sum != num3 and Ans == 0:
            score += 1
            print ("Score:", score)
    
    if Symbols_Chosen == "-":
        Diff = num1 - num2 
        print (num1 - num2 ,""="", num3)
        Ans = input ("1 for True, 0 for False")
        if Sum == num3 and Ans == 1:
            score += 1 
            print ("Score:", score)
        if Sum != num3 and Ans == 1:
           break 
            score += 0
            print ("== GAME OVER ==")
            print (" Your total score is ",score)
        if Sum == num3 and Ans == 0:
            break 
            score += 0
            print ("== GAME OVER ==")
            print (" Your total score is ",score)
        if Sum != num3 and Ans == 0:
            score += 1
            print ("Score:", score)
    
    if Symbols_Chosen == "/":
        Quotient = num1 - num2 
        print (num1 / num2 ,""="", num3)
        Ans = input ("1 for True, 0 for False")
        if Sum == num3 and Ans == 1:
            score += 1 
            print ("Score:", score)
        if Sum != num3 and Ans == 1:
            break 
            score += 0
            print ("== GAME OVER ==")
            print (" Your total score is ",score)
        if Sum == num3 and Ans == 0:
           break 
            score += 0
            print ("== GAME OVER ==")
            print (" Your total score is ",score)
        if Sum != num3 and Ans == 0:
            score += 1
            print ("Score:", score)
    
    
        
 




