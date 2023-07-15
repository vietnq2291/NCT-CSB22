import os 
import datetime

"""
#BT1: 
with open("Labs/Lab12/Submissions/Trung-Tin/names.txt", "r") as txtfile1: 
    nameList = txtfile1.readlines()
    print("\nList of names: ")
    for name in range(len(nameList)):
        print(f"- {nameList[name]}", end="")
    pass 
"""


"""
#BT2: 
cInput1 = input("\nInput file name: ")
existCon = os.path.exists(f"Labs/Lab12/Submissions/Trung-Tin/{cInput1}")
if existCon:
    with open(f"Labs/Lab12/Submissions/Trung-Tin/{cInput1}", "r") as txtfile2: 
        print("File content: ")
        fileContent = txtfile2.read()
        print(fileContent)
else: 
    print("File not found.")
"""

"""
#BT3: 
with open("Labs/Lab12/Submissions/Trung-Tin/user-inputs.txt", "a+") as txtfile3: 
    saveCond = 0
    while True:     
        uInput2 = input(">>> ")
        if uInput2 == "":
            saveCond += 1
            if saveCond >= 2:
                saveCond = 0
                txtfile3.seek(0)
                break
        elif uInput2 != "": 
            txtfile3.write(f"{uInput2}\n")
            
    txtfile3.seek(0)
    print("-- Input file content below -- ")
    fileLen = txtfile3.readlines()
    for line in range(len(fileLen)):
        print(fileLen[line], end="")
    print("-- Input recorded in user-inputs.txt --")
"""

"""
#BT4: 
with open("Labs/Lab12/Submissions/Trung-Tin/input-logs.txt", "a+") as txtfile4: 
    saveCond2 = 0
    recentLines = []
    getTime = datetime.datetime.now()
    txtfile4.write(f"-- Inputs at {getTime} --\n")
    while True:     
        uInput3 = input(">>> ")
        if uInput3 == "":
            saveCond2 += 1
            if saveCond2 >= 2:
                saveCond2 = 0
                txtfile4.seek(0)
                break
        elif uInput3 != "": 
            recentLines.append(uInput3)
            txtfile4.write(f"{uInput3}\n")
            
    txtfile4.seek(0)
    print("-- Input file content below -- ")
    for line in range(len(recentLines)):
        print(recentLines[line])
    recentLines = []
    print("-- Input recorded in user-inputs.txt --")
"""

""" 
#BT5: 
with open("Labs/Lab12/Submissions/Trung-Tin/question-bank.txt", "r") as txtfile5: 
    points = 0
    questionList = []
    procQuest = txtfile5.readlines()
    print(procQuest)
    for c in range(len(procQuest)):
        spQuest = f"{procQuest[c]}".split(",")
        questionList.append(spQuest)      
    print(questionList)
    print("Give the correct answers to get points.")
    for quest in range(len(questionList)):
        print(questionList[quest][0])
        answerLen = len(questionList[quest][1])
        uInput4 = int(input(""))
        if uInput4 == int(questionList[quest][1][0:answerLen-1]):
            points += 1
    print(f"-- You get {points}/{len(questionList)} points.")        
"""