#Bài 1:
def int():
    N = float(input())
    if N == N//1:
        print(f'{int(N)} số nguyên')
    else:
        print(f'{N} k là số nguyên')
int()
#Bài 2:
def prime():
    x = int(input('Nhập số:'))
    a = 0
    for i in range(1,x+1):
        if x%i == 0:
            a = a+1
    if a == 2:
        print(f'{x} là số nguyên tố')
    else:
        print(f'{x} k là số nguyên tố')
prime()
#Bài 3
arr = []
def prime(x):    
    a = 0
    for i in range(1,x+1):
        if x%i == 0:
            a = a+1
    if a == 2:
        arr.append(x)
        return True
N = int(input())
cnt = 0
x = 2
while N>cnt:
    prime(x)
    if prime(x)==True:
        cnt = cnt+1
    x = x+1
for t in arr:
    if arr.count(t) > 1:
        arr.remove(t)
        if t in arr:
            continue
print(arr)
#Bài 4
def giaithua(N):
    a = 1
    for i in range(1,N+1):
        a = a*i     
    return a
def bieuthuc():
    n = int(input())
    b = 0
    for y in range(1,n+1):
        b = b + giaithua(y)/y
    print(b)
bieuthuc()
#Bài 5
from datetime import *
day = date(2021,7,21)
hour = time (13,36,10)
print ('hôm nay: ',day.strftime ('%d/%m/%Y'))
print (f'giờ: {hour}')
