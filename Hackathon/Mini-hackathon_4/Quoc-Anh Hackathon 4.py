# Part 1

# Ex1
computers = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30 
}
# Ex2
print ("Available MACBOOKs:",computers['MACBOOK'])

brand = input ("Input a brand: ")
print (f'Available {brand}s: {computers[brand]}')

# Part 2

# Ex1
computers = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30 
}
computers ['TOSHIBA'] = 10
print ('Available products:')
for i in computers:
    print (f'- {i}: {computers[i]}')

# Ex2
brand_1 = input ("Input a brand: ")
amount = input ('Input amount: ')
computers [brand_1] = amount
print ('Available products:')
for i in computers:
    print (f'- {i}: {computers[i]}')

# Ex3
computers = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30 
}
computers ['DELL'] = 60
computers ['MACBOOK'] = 2
for i in computers:
    print (f'- {i}: {computers[i]}')

# Ex4
computers = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30 
}
sum = 0 
for i in computers:
    sum += computers[i]
print (f'Total products: {sum}')

# Part 3

# Ex1
computer_price = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK': 1200,
    'ASUS' : 400
}

# Ex2
print ("Price of ASUS:", computer_price['ASUS'])

# Ex3
brand_2 = input ("Input a brand: ")
print (f'Price of {brand_2}: {computer_price[brand_2]}')

# Part 4

# Ex1
computer_price = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK': 1200,
    'ASUS' : 400
}
print ("Total price:",5*computer_price['ASUS'])

# Ex2
brand_3 = input ("Input a brand: ")
amount_1 = int(input ("Input amount to buy: "))
print ("Total price:",amount_1 * computer_price[brand_3])

# Ex3
while True: 
 computer_price = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK': 1200,
    'ASUS' : 400
}
 computers = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30 
}
 brand_4 = input ("Input a brand: ")
 amount_2 = int(input ("Input amount to buy: "))
 print ("Total price:",amount_2 * computer_price[brand_4])
 computers [brand_4] -= amount_2
 print ('Available products:')
 for i in computers:
     print (f'- {i}: {computers[i]}')
#Part 5
# đoạn này có cái while true, có j anh chạy xong bỏ ra để chạy mấy cái code dưới nhé ạ
# Ex1
computer_price = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK': 1200,
    'ASUS' : 400
}
computers = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30 
 }
computer_value = {}
for i in computers:
    computers[i] = computers[i] * computer_price [i]
    computer_value[i] = computers[i]
print('Total values of available brands: ')
for x in computer_value:
    print (f'- {x}: {computer_value[x]}')

# Ex2
total_value = 0
for x in computer_value:
    total_value += computer_value[x]
print ("Total value of available items: ",total_value)

# Part 6

# Ex1
Character_Att = {
    'Name' : 'Light',
    'Age' : 17,
    'Strength' : 8,
    'Defense' : 10,
    'HP' : 100,
    "Backpack" : 'Shield, Breadloaf',
    'Gold' : 100,
    'Level' : 2
}

# Ex2
Character_Att['Gold'] += 50
print ("Gold:",Character_Att['Gold'])

# Ex3
Character_Att ['Backpack'] = 'Shield, Breadloaf, Flintstone'
print ("Backpack:",Character_Att['Backpack'])
        
# Part 7 + Part 8
import random as r 
Skill_1 ={
     'Name' : 'Tackle',
    'Minimum level' : 1,
    'Damage' : 5,
    'Hit rate' : 0.3
}

Skill_2 = {
    'Name' : 'Quick Attack',
    'Minimum level' : 2,
    'Damage' : 3,
    'Hit rate' : 0.5
}

Skill_3 = {
    'Name' : 'Strong Kick',
    'Minimum level' : 4,
    'Damage' : 9,
    'Hit rate' : 0.2
}
Skill_set = [Skill_1, Skill_2, Skill_3]
print ("Skill 1:",Skill_1['Name'])
print ('Skill 2:',Skill_2['Name'])
print ('Skill 3:',Skill_3['Name'])
Skill_input = int(input ("Choose skill by number: "))
Level_input = int(input("Input your level: "))
hit_rate = r.randint (0,1) 

if Skill_input == 1:
    if Level_input < Skill_1 ['Minimum level']:
     print ("Cannot deploy. Required level",Skill_1['Minimum level'])
    if hit_rate < Skill_1 ['Hit rate']:
     print ("Missed.")
    else: 
     print ("You chose",Skill_1['Name'])
     print ("Damage:",Skill_1 ['Damage'])

if Skill_input == 2:
    if Level_input < Skill_2 ['Minimum level']:
     print ("Cannot deploy. Required level",Skill_2['Minimum level'])
    if hit_rate < Skill_2 ['Hit rate']:
     print ("Missed.")
    else: 
     print ("You chose",Skill_2['Name'])
     print ("Damage:",Skill_2 ['Damage'])

if Skill_input == 3:
    if Level_input < Skill_3 ['Minimum level']:
     print ("Cannot deploy. Required level",Skill_3['Minimum level'])
    if hit_rate < Skill_3 ['Hit rate']:
     print ("Missed.")
    else: 
     print ("You chose",Skill_3['Name'])
     print ("Damage:",Skill_3 ['Damage'])



    
     














# Ex2



