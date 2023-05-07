import math
import turtle


#BT1: 
cRadius = float(input("Radius: "))
cPerimeter = 2*3.14*cRadius
cArea = 3.14*(cRadius**2)

print(f"Radius: {cRadius}\nPerimeter: {cPerimeter}\nArea: {cArea}")

#BT2: 
sqLen = int(input("Length of edge: "))
sqDiagLine = math.sqrt(sqLen**2+sqLen**2)
print(sqDiagLine)

#BT3: 
accName = input("Account name: ")
domName = input("Domain name: ")
print(f"Full Email: {accName}@{domName}")

#BT4:
cDay = int(input("Day: "))
cMonth = int(input("Month: "))
cYear = int(input("Year: "))
print(f"Date in MM/DD/YY format: {cMonth}/{cDay}/{cYear}")
print(f"Date in DD/MM/YY format: {cDay}/{cMonth}/{cYear}")

#BT5: 
depAmount = int(input("Deposit: "))
yearDeposited = int(input("Year: "))
calcProf = float(depAmount*(1.05)**yearDeposited)
print(f"Account after {yearDeposited} year: {calcProf}")

"""
#BT7:
turtle.pensize(10)
turtle.pencolor('#cf8f03')
turtle.left(30)
turtle.forward(120)
turtle.right(60)
turtle.forward(120)
turtle.right(120)
turtle.forward(120)
turtle.right(60)
turtle.forward(120)
turtle.penup()
turtle.goto(40, 0)
turtle.pendown()
turtle.pencolor('#0b2c3c')
turtle.right(120)
turtle.forward(120)
turtle.right(60)
turtle.forward(120)
turtle.right(120)
turtle.forward(120)
turtle.right(60)
turtle.forward(120)
"""
"""
#BT6: 
turtle.forward(120)
turtle.left(90)
turtle.forward(85)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(85)
turtle.left(180)
turtle.pencolor('#de5246')
turtle.pensize(10)
turtle.forward(85)
turtle.right(130)
turtle.forward(75)
turtle.left(80)
turtle.forward(75)
turtle.right(130)
turtle.forward(85)
"""
