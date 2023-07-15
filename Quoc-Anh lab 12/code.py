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

if os.path.exists(input) == True: 
    with open (input,'r') as file2:
        print ("File content:")
        content = file2.read
        print (content)
        pass
else: 
    print ("File not found.")
     