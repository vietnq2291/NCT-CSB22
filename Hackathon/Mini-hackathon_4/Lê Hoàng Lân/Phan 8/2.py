import random
skill1 = {'Name' :"Tackle", 'Minimum level': 1, 'Damge': 5, 'Hit rate': 0.3 }
skill2 = {'Name' :"Quick Attack", 'Minimum level': 2, 'Damge': 3, 'Hit rate':0.5 }
skill3 = {'Name' :"Strong Kick", 'Minimum level': 4, 'Damge': 9, 'Hit rate':0.2 }
chaskill = [skill1,skill2,skill3]
print(f"skill1: {skill1['Name']}")
print(f"skill2: {skill2['Name']}")
print(f"skill3: {skill3['Name']}")
n = int(input("Choose Skill: "))
level = 2

g = random.randint(0,1)
if n < level:
    print(f"You chose Tackle")
    if g > chaskill[n-1]['Hit rate']:
        print(f"Damge: {chaskill[n-1]['Damge']}")
    else: print("Missed.")
if n > level:
    print(f"You chose Strong Kick")
    print(f"Cannot deploy. Required level {chaskill[n-1]['Minimum level']}")
if n == level:
    print(f"You chose Quick Attack")
    if g > chaskill[n-1]['Hit rate']:
        print(f"Damge: {chaskill[n-1]['Damge']}")
    else: print("Missed.")