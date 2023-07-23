#Bài 1
n1 = int(input('Input first number: '))
n2 = int(input('Input second number: '))
print(f'{n1}+{n2}=1{n1+n2}')
#Bài 2
from math import*
a = int(input('input a: '))
b = int(input('input b: '))
c = int(input('input c: '))
delta = b**2-4*a*c
if a != 0:
    if delta == 0:
        print(f'x1=x2={-b/(2*a)}')
    if delta > 0:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        print(x1,x2)
    if delta < 0:
        print('no solution')
else:
    print('input again') 
#Bài 3
def reverse_string(str):  
    str1 = ""
    for i in str:  
        str1 = i + str1  
    return str1  
def  is_palindrome():
    str2 = input('input: ')
    if str2 == reverse_string(str2):
        print('palindrome')
    else:
        print('not palindrome')
is_palindrome()
#Bài 4
menu = ['Bun bo', 'Pho', 'Banh canh', 'Hu tiu']
arr = []
while True:
    order = input('Please choose a dish: ')
    if order in arr:
        print('You chose this already. Anything else? (y/n): ')
    if order in menu:
        arr.append(order)
    print('Great choice! Anything else? (y/n): ')
    yn = input()
    if yn == 'y':
        
        continue
    if yn == 'n':
        print('Well done! Your order:')
        break
for i in arr:
    print(i,'', end = '')         
#Bài 5
phone = {
    'Iphone12': 28000000,
    'Samsung N10': 16000000,
    'Oppo 93': 7500000,
    'Vsmart': 7400000,
    'Vivo': 4200000,
}
chonmay = input('Input name of a phone: ')
print(f'price of {chonmay}: {phone[chonmay]}')
budget = int(input('Input your budget: '))
for i in phone:
    if budget > phone[i]:
        print('-',i,':',phone[i])
#Bài 6
n = int(input('Input a number:'))
cnt = 1
while True:
    n = n//10
    cnt+=1
    if n//10 == 1:
        cnt+=1
        break
print(cnt)
#Bài 7
num = [5, 1, 8, 92, -1, 30]
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            a = num[i]
            num[i]=num[j]
            num[j]=a
for x in num:
    print(x, end=' ')
#Bài 8
arr = [1,1]
a = 0 
n = int(input('Input a number:'))
for i in range(n-2):
    a = arr[i]+ arr[i+1]
    arr.append(a)
for i in arr:
    print(i, end=' ')
