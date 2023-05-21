import turtle

#BT1: 
cStairs = int(input("Number: "))
for x in range(cStairs):
    print("#"*(x+1)) 

#BT2: 
while True: 
    cReal = float(input("Input a positive number: "))
    if cReal > 0: 
        print("Thank you.")
        break

#BT3: 
cNum = int(input("Number: "))
if cNum >= 1:
    res = 1
    for x in range(1, cNum+1):
        res = res * x
    print(f"{cNum}! = {res}")
elif cNum == 0:
    print(f"0! = 1")
else:
    print("Invalid")

#BT4: 
cNum2 = int(input("Number: "))
res2 = 0
for x in range(len(str(cNum2))):
    res2 += int(str(cNum2)[x])
print(res2)

#BT5:
maxVal = 0
res3 = 0
result = " "
for y in range(1000, 9999):
    for z in range(len(str(y))):
        res3 += int(str(y)[z])
    if res3 == 9:
        result += f"{str(y)} " 
        maxVal += 1
        if maxVal == 10:
            break
    else: 
        res3 = 0
print("Numbers with sum of digits = 9: \n", result)

#BT6: 
cEdge = int(input("Number of edges: "))
if cEdge > 2:
    if cEdge == 3: 
        rotDeg = 180 - (180/cEdge)
        print(rotDeg)
        for x in range(cEdge):
            turtle.forward(100)
            turtle.right(rotDeg)
    elif cEdge > 3:
        rotDeg = 360 - (cEdge-1)*(360/cEdge)
        print(rotDeg)
        for x in range(cEdge):
            turtle.forward(100)
            turtle.right(rotDeg)
        

#BT7: 
#r = 0
#while True: 
#    r += 10
#    turtle.circle(r, 180, 10)
#    if r == 180:
#        break