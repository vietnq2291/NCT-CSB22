import random
#BT1: 
reserved = {
    "HP": 20, 
    "DELL": 50, 
    "MACBOOK": 12, 
    "ASUS": 30
}

print(reserved["MACBOOK"])
uInput1 = input("Input a brand: ")
if uInput1 in reserved.keys():
    print(f"Available {uInput1}s: {reserved[uInput1]}")
else: 
    print("Not found.")

#BT2: 
reserved["TOSHIBA"] = 10
print("Available products: ")
for item in reserved.keys():
    print(f"- {item}: {reserved[item]}")

uInput2 = input("Input a brand: ")
uInput3 = int(input("Input amount: "))
reserved[uInput2] = uInput3
print("Available products: ")
for item in reserved.keys():
    print(f"- {item}: {reserved[item]}")

reserved["TOSHIBA"] = 60
reserved["MACBOOK"] = 2
print("Available products: ")
for item in reserved.keys():
    print(f"- {item}: {reserved[item]}")

reserved2 = {
    "HP": 20, 
    "DELL": 50, 
    "MACBOOK": 12, 
    "ASUS": 30
}
base = 0 
for item in reserved2.items():
    base += item[1]
print(f"Total products: {base}")


#BT3: 

prices = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400,
}
print(f"Prices of ASUS: {prices['ASUS']}")

cInput4 = input("Input a brand: ")
print(f"Price of {cInput4}: {prices[cInput4]}")

#BT4: 
reserved3 = {
    "HP": 20, 
    "DELL": 50, 
    "MACBOOK": 12, 
    "ASUS": 30
}
print(f"Total prices: {prices['ASUS']*5}")

cInput5 = input("Input a brand: ")
cInput6 = int(input("Input amount: "))
print(f"Total prices: {prices[cInput5]*cInput6}")

cInput7 = input("Input a brand: ")
cInput8 = int(input("Input amount to buy: "))
cInput9 = input(f"Total prices: {prices[cInput7]*cInput8}")
reserved3[cInput7] -= cInput8

print("Available products: ")
for item in reserved3.keys():
    print(f"- {item}: {reserved3[item]}")

#BT5: 
reserved4 = {
    "HP": 20, 
    "DELL": 50, 
    "MACBOOK": 12, 
    "ASUS": 30
}
for item in reserved4.keys():
    reserved3[item] = reserved4[item]*prices[item]

print("Available products: ")
for brand in reserved4.keys():
    print(f"- {brand}: {reserved4[brand]}")

base2 = 0
for item in reserved4.items():
    base2 += item[1]
print(f"Total value of available items: {base2}")






#BT6: 
character = {
    "Name": "Light", 
    "Age": 17, 
    "Strength": 8, 
    "Defense": 10, 
    "HP": 100, 
    "Backpack": ["Shield", "Bread Loaf"], 
    "Gold": 100, 
    "Level": 2,
}
character["Gold"] += 50
print(f"Gold: {character['Gold']}")

character["Backpack"].append("FlintStone")

itemList = ""
for item in character['Backpack']:
    itemList += f"{item} "
print(f"Backpack: {itemList}.")

#BT7: 
skill1 = {
    "name": "Tackle",
    "minLvl": 1,
    "damage": 5,
    "hitRate": 0.3
}
skill2 = {
    "name": "Quick Attack",
    "minLvl": 2,
    "damage": 3,
    "hitRate": 0.5
}
skill3 = {
    "name": "Strong Kick",
    "minLvl": 4,
    "damage": 9,
    "hitRate": 0.2
}
charSkills = [skill1, skill2, skill3]

while True: 
    for skill in range(len(charSkills)):
        print(f"Skill {skill+1}: {str(charSkills[skill]['name'])}")
    cInput10 = int(input("Choose skill by number: "))
    if cInput10 == "quit":
        break
    for chosenSkill in range(len(charSkills)):
        if chosenSkill == cInput10-1:
            if charSkills[chosenSkill]['minLvl'] <= character["Level"]:
                print(f"\nYou chose {charSkills[chosenSkill]['name']}.")
                hit = random.random()
                print(hit)
                if hit <= charSkills[chosenSkill]['hitRate']:
                    print(f"Damage: {charSkills[chosenSkill]['damage']}\n")
                else:
                    print("Missed.\n")
            else:
                print(f"\nYou chose {charSkills[chosenSkill]['name']}.")
                print(f"Cannot deploy. Required level {charSkills[chosenSkill]['minLvl']}.\n")
