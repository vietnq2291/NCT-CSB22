import math


#BT1: 
uInput1 = int(input("\nFirst number: "))
uInput2 = int(input("Second number: "))
print(uInput1 + uInput2)

#BT2: 
uInput3 = int(input("a: "))
uInput4 = int(input("b: "))
uInput5 = int(input("c: "))
delta = uInput4**2 - 4*uInput3*uInput5
if delta == 0:
    print(f"The equation has 1 solutions.\nx = {-uInput4/2*uInput3}")
elif delta > 0: 
    res1 = ((-uInput4 + math.sqrt(delta))/2*uInput3)
    res2 = ((-uInput4 - math.sqrt(delta))/2*uInput3)
    print(f"The equation has 2 solutions.\nx = {res1} or x = {res2}")
else: 
    print("The equation has no solutions.")

#BT3:
uInput6 = input("Input a text: ") 
def is_palindrome(sample): 
    if sample == sample[::-1]:
        print("This is a palindrome.")
    else: 
        print("This is not a palindrome.")
is_palindrome(uInput6)

#BT4: 
print("== Welcome to MindX restaurant ==")
foodList = []
while True: 
    fSelect = input("Please choose a dish: ")
    if fSelect not in foodList:
        foodList.append(fSelect)
        aSelect = input("Great choice! Anything else? (y/n): ")
        aSelect.lower()
        if aSelect == "y":
            continue
        elif aSelect == "n":
            print("Well done! Your order: ")
            for food in foodList: 
                print(f"- {food}")
            break
    elif fSelect in foodList:
        aSelect2 = input("You chose this already. Anything else? (y/n): ")
        aSelect2.lower()
        if aSelect == "y":
            continue
        elif aSelect == "n":
            print("Well done! Your order: ")
            for food in foodList: 
                print(f"- {food}")
            break


#BT5: 
phoneDict = {
    "Iphone12": 28000000, 
    "Samsung N10": 16000000,
    "Oppo 93": 7500000,
    "Vsmart": 7400000,
    "Vivo": 4200000
}
print("List of available phones: ")
for key in phoneDict.keys():
    print(f"- {key}")

phoneSelect = input("\nInput name of a phone: ")
def firstProgram(phone):
    print(f"\nPrice of {phone}: {phoneDict[phone]}")
firstProgram(phoneSelect)

uBudget = int(input("\nInput your budget: "))
def secondProgram(budget): 
    print("\nPhones that fit your budget: ")
    for key, value in phoneDict.items():
        if value <= budget: 
            print(f"- {key}: {phoneDict[key]}")        
secondProgram(uBudget)

#BT6: 
iInput = int(input("Input a number: "))
if iInput > 0: 
    print(f"This number has {len(str(iInput))} digit(s).")

#BT7: 
baseList = [5, 1 , 8, 92, -1, 30]
base = baseList[0]
lowest = 0
sortedList = []

for num in baseList[:]:
    if base > num: 
        if num < lowest:
            lowest = num
            sortedList.insert(0, num)
        else:
            sortedList.append(num)
        baseList.remove(num)
    elif base < num: 
        sortedList.append(base)
        baseList.remove(base)
        base = num
sortedList.append(baseList[0])
print(sortedList)

#BT8: 
seqInput = int(input("Input a number: "))
base = 0 
next = 1 
sum = 0 
result = ""
for i in range(seqInput):
    sum = base + next 
    base = next 
    next = sum 
    result += str(f"{next} ")
print(f"{result}")


