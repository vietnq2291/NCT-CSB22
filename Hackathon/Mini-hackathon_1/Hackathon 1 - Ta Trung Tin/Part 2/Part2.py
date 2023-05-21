import turtle

#BT1: 
for x in range(3, 13):
    print(x)

#BT2: 
cNum = int(input("Number: "))
if cNum > 0:
    for x in range(0, cNum+1):
        print(x)

#BT3: 
cNum2 = int(input("Number: "))
if cNum2 > 0:
    for x in range(1, cNum2+1, 2):
        print(x)

#BT4: 
cEdges = int(input("Edges: "))
if cEdges > 2:
    if cEdges == 3:
        rotDeg = 180 - (180/cEdges)
        for x in range(cEdges):
            turtle.forward(100)
            turtle.right(rotDeg)
    elif cEdges > 3:
        rotDeg = 360 - (cEdges-1)*(360/cEdges)
        for x in range(cEdges):
            turtle.forward(100)
            turtle.right(rotDeg)

