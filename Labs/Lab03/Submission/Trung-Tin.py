import math
#BT1:
rNum = int(input(">> "))
if rNum % 2 == 0:
    print(f"{rNum} is even")
else:
    print(f"{rNum} is odd")
#BT2: 
rNum2 = float(input(">> "))
if rNum2.is_integer() == True:
    print(f"{int(rNum2)} is an integer")
else:
    print(f"{rNum2} is not an integer")
    
#BT3: 
rInput = input("Character: ")
if rInput.isdigit() == True:
    print(f"{rInput} is a digit")
else:
    print(f"{rInput} is not a digit")
        
#BT4: 
rNum3 = float(input(">> "))
if rNum3 % 3 == 0 and rNum3 % 5 == 0:
    print(f"{rNum3} is divisible by 3 and 5.") 
elif rNum3 % 3 == 0 and rNum3 % 5 != 0:
    print(f"{rNum3} is divisible by 3") 
elif rNum3 % 5 == 0 and rNum3 % 3 != 0:
    print(f"{rNum3} is divisible by 5.") 
else:
    print(f"{rNum3} is not divisible by 3 and 5.") 

#BT5: 
cUser = "admin"
cPass = "12345"
print("Security System")
uInput = input("Username: ")
pInput = input("Password: ")
if uInput == cUser and pInput == cPass:
    print("Logged in.")
elif uInput != cUser or pInput != cPass:
    print("Wrong username or password.")

#BT6:
len1 = int(input("Length 1: "))
len2 = int(input("Length 2: "))
len3 = int(input("Length 3: "))
if len1 != 0 and len2 != 0 and len3 != 0:
    sum1 = len1 + len2
    sum2 = len1 + len3
    sum3 = len2 + len3
    if (sum1 > len3) and (sum2 > len2) and (sum3 > len1):
        print("The 3 line segments can form a triangle.")
    else:
        print("The 3 line segments cannot form a triangle.")
else:
    print("Invalid.")

#BT7: 
len1_2 = int(input("Length 1: "))
len2_2 = int(input("Length 2: "))
len3_2 = int(input("Length 3: "))
if len1_2 != 0 and len2_2 != 0 and len3_2 != 0:
    sum1 = len1_2 + len2_2
    sum2 = len1_2 + len3_2
    sum3 = len2_2 + len3_2
    if (sum1 > len3_2) and (sum2 > len2_2) and (sum3 > len1_2):
        print("The 3 line segments can form a ")
        if (len1_2 == math.sqrt(len2_2*2 + len3_2*2)) or (len2_2 == math.sqrt(len1_2*2 + len3_2*2)) or (len3_2 == math.sqrt(len1_2*2 + len2_2*2)):
            print("right triangle.")
        elif len1_2 == len2_2 == len3_2:
            print("equilateral traingle.")
        else:
            print("triangle.")
    else:
        print("The 3 line segments cannot form a triangle.")
else:
    print("Invalid.")