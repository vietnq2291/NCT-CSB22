#Phần 1
#Bài 1
maytinh = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
#Bài 2
maytinh = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
print(f'Available MACBOOKs: {maytinh["MACBOOK"]}')
#Bài 3
maytinh = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
chon = input('input a brand:')
print(f'Available {chon}s:{maytinh[chon]}')
#Phần 2
#Bài 1
maytinh = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
maytinh['TOSHIBA'] = 10
for i in maytinh:
    print(i,':',maytinh[i])
#Bài 2
maytinh = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
loaimay = input('input a brand:')
somay = int(input('input amount'))
maytinh[loaimay] = somay
for i in maytinh:
    print(i,':',maytinh[i])
#Bài 4
maytinh = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
n = 0
for i in maytinh.values():
    n = n + i
print(f'Total products:{n}')
#Bài 3
maytinh = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
maytinh['DELL'] = maytinh['DELL'] + 10
maytinh['MACBOOK'] = maytinh['MACBOOK'] - 2
for i in maytinh:
    print(i,':',maytinh[i])
#Phần 3
#Bài 1
giamaytinh = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}
#Bài 2
giamaytinh = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400,
}
print(f'rice of ASUS: {giamaytinh["ASUS"]}')
#Bài 3
giamaytinh = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400,
}
chonmay = input('Input a brand:')
print(f'Price of {chonmay}s: {giamaytinh[chonmay]}')
#Phần 4
#Bài 1
giamaytinh = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400,
}
print(f'Total price: {giamaytinh["ASUS"]*5}')
#Bài 2
giamaytinh = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400,
}
chonmuamay = input("Input a brand: ")
soluongmay = int(input('Input amount to buy: '))
print(f'Total price: {giamaytinh[chonmuamay]*soluongmay}')
#Bài 3
maytinh = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
giamaytinh = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400,
}
chonmuamay = input("Input a brand: ")
soluongmay = int(input('Input amount to buy: '))
print(f'Total price: {giamaytinh[chonmuamay]*soluongmay}')
maytinh[chonmuamay] = maytinh[chonmuamay] - soluongmay
print('Available products:')
for i in maytinh:
    print(i,':',maytinh[i])
#Phần 5
#Bài 1
maytinh = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
giamaytinh = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400,
}
print('Total value of available brands: ')
for i in maytinh:
    print(f'{i}',":",f'{maytinh[i]*giamaytinh[i]}')
#Bài 2
maytinh = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
giamaytinh = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400,
}
n = 0
for i in maytinh:
    n = n + maytinh[i]*giamaytinh[i]
print(f'Total value of available items: {n}')
#Phần 6
#Bài 1
nhanvat = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': 'Shield, Bread, Loaf',
    'Gold': 100,
    'Level': 2
}
#Bài 2
nhanvat = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': 'Shield, Bread, Loaf',
    'Gold': 100,
    'Level': 2
}
nhanvat["Gold"] = nhanvat["Gold"] + 50
print(f'Gold: {nhanvat["Gold"]}')
#Bài 3
nhanvat = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': 'Shield, Bread, Loaf',
    'Gold': 100,
    'Level': 2
}
nhanvat["Backpack"] = nhanvat["Backpack"] + ", FlintStone"
print(f'Backpack: {nhanvat["Backpack"]}')
#Phần 7
#Bài 1
skill1 = {
    'Name': 'Tackle', 
    'Minimum level': 1, 
    'Damage': 5, 
    'Hit rate': 0.3
}
skill2 = {
    'Name': 'Quick Attack',
    'Minimum level': 2, 
    'Damage': 3, 
    'Hit rate': 0.5
}
skill3 = {
    'Name': 'Strong Kick', 
    'Minimum level': 4, 
    'Damage': 9, 
    'Hit rate': 0.2
}
#Bài 2
skill1 = {
    'Name': 'Tackle', 
    'Minimum level': 1, 
    'Damage': 5, 
    'Hit rate': 0.3
}
skill2 = {
    'Name': 'Quick Attack',
    'Minimum level': 2, 
    'Damage': 3, 
    'Hit rate': 0.5
}
skill3 = {
    'Name': 'Strong Kick', 
    'Minimum level': 4, 
    'Damage': 9, 
    'Hit rate': 0.2
}
print(f'Skill 1: {skill1["Name"]}')
print(f'Skill 2: {skill2["Name"]}')
print(f'Skill 3: {skill3["Name"]}')
#Phần 8
#Bài 1
skill1 = {
    'Name': 'Tackle', 
    'Minimum level': 1, 
    'Damage': 5, 
    'Hit rate': 0.3
}
skill2 = {
    'Name': 'Quick Attack',
    'Minimum level': 2, 
    'Damage': 3, 
    'Hit rate': 0.5
}
skill3 = {
    'Name': 'Strong Kick', 
    'Minimum level': 4, 
    'Damage': 9, 
    'Hit rate': 0.2
}
print(f'Skill 1: {skill1["Name"]}')
print(f'Skill 2: {skill2["Name"]}')
print(f'Skill 3: {skill3["Name"]}')
skill = int(input('Choose skill by number:'))
if skill == 1:
    print(f'You choose {skill1["Name"]}')
    print(f'Damage: {skill1["Damage"]}')
if skill == 2:
    print(f'You choose {skill2["Name"]}')
    print(f'Damage: {skill2["Damage"]}')
if skill == 3:
    print('Cannot deploy. Required level 4.')
    print('Missed')
#Bài 2
skill1 = {
    'Name': 'Tackle', 
    'Minimum level': 1, 
    'Damage': 5, 
    'Hit rate': 0.3
}
skill2 = {
    'Name': 'Quick Attack',
    'Minimum level': 2, 
    'Damage': 3, 
    'Hit rate': 0.5
}
skill3 = {
    'Name': 'Strong Kick', 
    'Minimum level': 4, 
    'Damage': 9, 
    'Hit rate': 0.2
}
print(f'Skill 1: {skill1["Name"]}')
print(f'Skill 2: {skill2["Name"]}')
print(f'Skill 3: {skill3["Name"]}')
skill = int(input('Choose skill by number:'))
import random
n = random.random()
if skill == 1 and skill1['Hit rate']>n:
    print(f'You choose {skill1["Name"]}')
    print(f'Damage: {skill1["Damage"]}')
if skill == 1 and skill1['Hit rate']<n:
    print(f'You choose {skill1["Name"]}')
    print('Missed')

if skill == 2 and skill2['Hit rate']>n:
    print(f'You choose {skill2["Name"]}')
    print(f'Damage: {skill2["Damage"]}')
if skill == 2 and skill2['Hit rate']<n:
    print(f'You choose {skill2["Name"]}')
    print('Missed')

if skill == 3 and skill3['Hit rate']>n:
    print(f'You choose {skill3["Name"]}')
    print(f'Damage: {skill3["Damage"]}')
if skill == 3 and skill3['Hit rate']<n:
    print(f'You choose {skill3["Name"]}')
    print('Missed')       





