

#BT1: 
print("== Registration ==")
cUsername = input("Username: ")
cPass = input("Password: ")
cEmail = input("Email: ")
print("Registered successfully.")

#BT2:
print("== Registration ==")
cUsername2 = input("Username: ")
while True:
    cPass2 = input("Password: ")
    cPassRe = input("Repeat password: ")
    if cPass2 == cPassRe:
        break
    else:
        print("Password not match. Please input again.")
cEmail2 = input("Email: ")       
print("Registered successfully.")

#BT3: 
print("== Registration ==")
cUsername3 = input("Username: ")
while True:
    cPass3 = input("Password: ")
    if len(cPass3) < 8:
        print("Invalid password. Please input again.")
    else: 
        cDigits = 0
        cLetters = 0
        for x in range(len(cPass3)):
            if cPass3[x].isdigit():
                cDigits += 1
            elif type(cPass3[x]) == str:
                cLetters += 1 
        if cDigits > 0 and cLetters > 0:
            cPassRe2 = input("Repeat password: ")
            if cPass3 == cPassRe2:
                break
            else:
                print("Password not match. Please input again.")
        else: 
            print("Invalid password. Please input again.")
cond1 = 0
cond2 = 0
while True:
    cEmail2 = input("Email: ")  
    for y in range(len(cEmail2)):
        if cEmail2[y] == "@":
            cond1 = 1
        elif cEmail2[y] == ".":
            cond2 = 1
    if cond1 == 1 and cond2 == 1:
            break
    else: 
        print("Invalid Email. Please input again.")

print("Registered successfully.")
