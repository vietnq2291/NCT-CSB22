# # BT1
# with open ("names.txt",'r') as file1:
#  name_list = file1.readlines()
#  print ("List of names:")
#  for i in range(len(name_list)):
#      print (f'- {name_list[i]}', end ='')
#  pass

# BT2
import os.path
input = input("Input file name: ")
file_exists = os.path.exists(input)
if  file_exists: 
    with open (input,'r') as file2:
        print ("File content:")
        content = file2.read
        print (content)
        pass
else: 
    print ("File not found.")

# BT3
print ('== Input file content below ==')
with open ('user-inputs.txt','r') as file3:
    opened = 0
    while True:
        user_Input = input (">> ")
        if user_Input == "":
            opened += 1
            if opened >=2:
                opened = 0
                file3.seek (0)
                break
        else: 
            file3.write (user_Input)
    file3.seek (0)
    print_input = file3.readlines()
    for i in range(len(print_input)):
        print ({print_input[i]}, end ='')
    print ('== Input recorded in user-inputs.text ==')

# BT4
from datetime import *


print ('== Input file content below ==')
with open ('input-logs.txt','r') as file4:
    file_time = datetime.now 
    file4.write (f'== Inputs at {file_time} ==')
    opened = 0
    while True:
        user_Input = input (">> ")
        if user_Input == "":
            opened += 1
            if opened >=2:
                opened = 0
                file4.seek (0)
                break
        else: 
         file4.write (user_Input)
    file4.seek (0)
    print_input2 = file4.readlines()
    for i in range(len(print_input)):
        print ({print_input[i]}, end ='')
    print ('== Input recorded in user-inputs.text ==')
    
# BT5
with open("question-bank.txt", "r") as file5: 
    point = 0
    question_list = []
    read_quest = file5.readlines()
    print(read_quest)
    for c in range(len(read_quest)):
        spQuest = f"{read_quest[c]}".split(",")
        question_list.append(spQuest)      
    print(question_list)
    print("Give the correct answers to get points.")
    for q in range(len(question_list)):
        print(question_list[q][0])
        answer = len(question_list[q][1])
        user_answer = int(input(""))
        if user_answer == int(question_list[q][1][0:answer-1]):
            point += 1
    print(f"-- You get {point}/{len(question_list)} points.") 