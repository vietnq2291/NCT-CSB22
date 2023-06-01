#BT1
Input = int(input("Input number: "))
for a in range (0 ,Input):
 a = a + 1
 print ("#" * a ) 

#BT2
Real_Number = float (input("Input a positive number: "))
while Real_Number <= 0:
    Real_Number = float (input("Input a positive number: "))
    
print ("Thank you.")  
 


#BT3
Input = int(input("Input number: "))
if Input < 0: 
    print ("Invalid")
elif Input == 0:
    print ("0! = 1")
elif Input > 0:
    for i in range (1,Input - 1):
#          print (Input, "!", "=", Input * i)
   
#BT4
Input = int(input("Input number: "))

i = 0
for x in range(len(str(Input))):
 i += int(str(Input)[x])
    
print (i)

BT5

for x in range (1000,9999):
    y = 0
    y_1 = 0 
    y_2 = " "
    for z in range(len(str(x))):
        y += int(str(x)[z])
        if y == 9:
            y_1 += 1
            y_2 += str (x)
            if y_1 == 10:
                break
        else: 
            y_2 += 0
print ("Number with sum of digits = 9: ")

#BT6
from turtle import *
a = int (input("Input number of edges:"))

while a <= 2:
    a = int (input("Input number of edges:"))

if a >= 3:
    for x in range (a)
    Turtle.forward (100)
    Turtle.right ((a-2)*180/a)

#BT7
from turtle import *
r = 0 
while True:
    r += 1
    circle (r,180)
    if r == 180:
        break
    
    
    

    
    
    



    
    