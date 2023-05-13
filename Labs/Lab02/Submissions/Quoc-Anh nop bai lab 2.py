#BT1
r = float (input ("Radius: "))
print ("Perimeter:", 2*3.1416*r) 
print ("Area:", 3.1416*r*r)

#BT2
from math import *
a = float (input("Length of edge: "))
print ("Length of diagonal line:", sqrt(a*a*2))

#BT3
Acc = input ("Account name: ")
Dom = input ("Domain name: ")
print ("Full name: ", Acc, "@", Dom)

#BT4
D1 = input("Date in MM/DD/YYYY format: ")
D1F = D1.split ("/")
print (f"Date in DD/MM/YYYY format: {D1F[1]}/{D1F[0]}/{D1F[2]}")

#BT5
from math import *
D = float (input("Deposit:"))
print ("Account after 1 year: ", D*105/100)
print ("Account after 5 years: ", D*105/100*105/100)
print ("Account after 10 years: ", D* pow(105/100, 10) )

#BT6
import turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.left (45)
t.pencolor ('#de5246')
t.pensize (10)
t.forward (150)
t.right (135)
t.forward (200)
t.right (90)
t.pencolor ("#000000")
t.pensize (2)
t.forward (215)
t.pensize (10)
t.pencolor ('#de5246')
t.right (90)
t.forward (200)
t.right(135)
t.forward (150)
t.left (135)
t.penup()
t.forward (110)
t.pendown()
t.left (90)
t.pencolor ('#000000')
t.pensize (2)
t.forward (107.5)
t.backward (215)
t.penup ()
t.forward (107.5)
t.right(90)
t.forward (30)

#BT7
import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.pensize (10)
t.pencolor ("0b2c3c")
t.penup ()
t.forward (100)
t.left (150)
t.pendown ()
t.forward (100)
t.left (60)
t.forward (100)
t.left (120)
t.forward (100)
t.left (60)
t.forward (100)
t.penup ()
t.left (150)
t.forward (90)
t.pendown ()
t.pencolor ("#cf8fo3")
t.left (150)
t.pendown ()
t.forward (100)
t.left (60)
t.forward (100)
t.left (120)
t.forward (100)
t.left (60)
t.forward (100)
