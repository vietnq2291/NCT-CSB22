#Phần 1 
#Bài 1
def chan():
    n = int(input())
    if n%2==0:
        print(f'{n} là số chẵn')
    else:
        print(f'{n} k là số chẵn')
chan()
#Bài 2
def cal_area():
    n = float(input('Bán kính:'))
    pi = 3.14
    print(f'{n*pi} là diện tích hình tròn')
cal_area()
#Bài 3
def reverse_string():  
    str1 = ""
    str = input()   
    for i in str:  
        str1 = i + str1  
    print(str1)   
reverse_string()   
#Bài 4
def reverse_string(str):  
    str1 = ""
    for i in str:  
        str1 = i + str1  
    return str1  
def  is_palindrome():
    str2 = input()
    if str2 == reverse_string(str2):
        print('palindrome')
#Phần 2
#Bài 1
def giaithua():
    n = int(input())
    a = 1
    for i in range(1,n+1):
        a = a*i
    print(a)
giaithua()
#Bài 3
arr = [1,1]
a = 0 
n = int(input())
for i in range(n-2):
    a = arr[i]+ arr[i+1]
    arr.append(a)
for i in arr:
    print(i, end=' ')
#Bài 2
num = [5, 1, 8, 92, -1, 30]
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            a = num[i]
            num[i]=num[j]
            num[j]=a
for x in num:
    print(x, end=' ')
#Phần3
import msvcrt
ch = msvcrt.getch().decode('utf-8')
l1 = ['-','-','-','P','-','-','-','-',]
l2 = ['-','-','-','-','-','-','-','-',]
l3 = ['-','-','-','-','-','K','-','-',]
l4 = ['-','-','-','-','-','-','-','-',]
l5 = ['-','-','-','-','D','-','-','-',]
print('== The ecscape game')
move = input()
def S():
    if move == 'S':
        l2.insert(l1.index('P'),'P')
        l1.remove("P")
        l1.insert(l1.index('P'),'-')
        print(l1)
        print(l2)
        print(l3)
        print(l4)
def W():
    if move == 'W':
        l2.insert(l1.index('P'),'P')
        l1.remove("P")
        l1.insert(l1.index('P'),'-')
        print(l1)
        print(l2)
        print(l3)
        print(l4)
        


