import turtle
#Part 1: 
c_list = ["red", "green", "blue"]
res1 = ""
for x in c_list:
    res1 += f"{x} "
print(res1)
res1 = ""

addColor = input("Input a new color: ")
c_list.append(addColor)

for x in c_list:
    res1 += f" {x}"
print(res1)

#Part2 :
c_list2 = ["red", "green", "blue"]
cPos = int(input("Input position (0 - 2): "))
print(c_list2[cPos])

cDel = int(input("Item to delete (0 - 2): "))
c_list2.pop(cDel)
res2 = ""
for x in c_list2:
    res2 += f"{x} "
print(res2)
res2 = ""

c_list3 = ["red", "green", "blue", "yellow", "violet", "orange"]
for x in range(len(c_list3)):
    turtle.color(c_list3[x])
    turtle.forward(50)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()


    
#Part 3:
n_list = [5, 1, 8, 92, -1, 30]
foundIdx = 0
selectNum = int(input("Input a number: "))
for x in range(len(n_list)):
    if selectNum == n_list[x]:
        foundIdx = x
        print(f"Number found at position: {foundIdx}.")
    else:
        print("Number not found.")

n_list2 = [5, 1, 8, 92, -1, 30]
sum = 0
for x in n_list2: 
    sum += x
print(sum)


n_list3 = []
sum2 = 0 
while True:
    n_Input = int(input("Enter numbers: "))
    if n_Input != 0:
        n_list3.append(n_Input)
    else: 
        for x in n_list3:
            sum2 += x
        break
print(f"Sume of list: {sum2}")


#Part 4: 
n_list4 = [5, 1, 8, 92, 7, 30]
res3 = ""
for x in n_list4:
    if x % 2 == 0:
        res3 += f" {x}"
print(f"Even numbers are:{res3}.")        


n_list5 = []
res4 = "" 
while True:
    n_Input2 = int(input("Enter numbers: "))
    if n_Input2 != 0:
        n_list5.append(n_Input2)
    else: 
        for x in n_list5:
            if x % 2 == 0:
                res4 += f" {x}"
        break
print(f"Even numbers are:{res4}.")



#Part 5: 
districts = ["BD", "BTL", "CG", "DD",  "HBT"]
populations = [247100, 333300, 266800, 420900, 318000]
most = 0
least = populations[0]
for x in range(len(districts)-1):
    if populations[x] > populations[x+1]:
        most = populations[x]
for y in range(0, len(districts)-1):
    if populations[y+1] < least:
        least = populations[y+1]
mostIdx = populations.index(most)
leastIdx = populations.index(least)
print(f"Indices of: \n- Most populated dist.: {mostIdx}\n- Least populated dist.: {leastIdx}")
print(f"Names of: \n- Most populated dist.: {districts[mostIdx]}\n- Least populated dist.: {districts[leastIdx]}")


#Part6: 
districts2 = ["BD", "BTL", "CG", "DD",  "HBT", ]
populations2 = [247100, 333300, 266800, 420900,  318000]
dt = [9.224, 43.35, 12.04, 9.96, 10.09]

denSum = 0
distSum = len(districts2)
print("Population density of: ")
for x in range(len(districts2)):
    density = populations2[x]/dt[x]
    denSum += density
    print(f"- {districts2[x]}: {density}")

avgPopDen = denSum/distSum
print(f"Average population density: {avgPopDen}")
        

#BT7: 
highScore = [78, 56, 67]
print("High scores: ")
for x in range(len(highScore)):
    print(f"{x+1}. {highScore[x]}.")   

newScore = int(input("Input new score: "))
highScore.append(newScore)
print("High scores: ")
for x in range(len(highScore)):
    print(f"{x+1}. {highScore[x]}.")   




#BT8: 
highScore3 = [78, 70, 67, 56, 45]
n_Input3 = int(input("Input new score: "))
print("High scores: ")
if n_Input3 > highScore3[-1]:
    highScore3.pop(-1)
    highScore3.append(n_Input3)
    sortedScore2 = sorted(highScore3)
    sortedScore2.reverse()
    for x in range(len(sortedScore2)):
        print(f"{x+1}. {sortedScore2[x]}")
else: 
    for x in range(len(highScore3)):
        print(f"{x+1}. {highScore3[x]}")


highScore2 = [78, 56, 67]
sortedScore = sorted(highScore2)
sortedScore.reverse()
print("High scores: ")
for x in range(len(sortedScore)):
    print(f"{x+1}. {sortedScore[x]}")