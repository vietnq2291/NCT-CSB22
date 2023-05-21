#Phần 1
#Bài 1
FN = input('Tên:')
LN = input('Họ:')
Full = FN + LN
print(Full)
#Bài 2
N = input("Nhập:")
print(N.upper())
#Bài 3
n = float(input())
n = n**2
print(n)
#Bài 4
import turtle
r = float(input())
htr = turtle.Turtle
htr.circle(r)
#Phần 2
#Bài 1
for i in range(3,13):
    print(i)
#Bài 2
N = int(input())
for i in range(N+1):
    print(i)
#Bài 3
so = int(input())
z = 0
y = -1
while so>y+2:
    z = z+1
    y = y+2 
    print(y)
#Bài 4
canh = float(input())
import turtle
turtle.forward(canh)
turtle.right(60)
turtle.forward(canh)
turtle.right(60)
turtle.forward(canh)
turtle.right(60)
turtle.forward(canh)
turtle.right(60)
turtle.forward(canh)
turtle.right(60)
turtle.forward(canh)
turtle.right(60)
turtle.mainloop()
#Phần 3
#Bài 1
a = float(input('nhập số bất kì:'))
if a > 13:
    print('số này lớn hơn 13')
else:
    print('số này bé hơn 13')
#Bài 2
A = int(input('nhập số bất kì'))
if A%2==0:
    print('số chắn')
else:
    print('không số chẵn')
#Bài 3
dd = int(input("Ngày:"))
mm = int(input("Tháng:"))
yy = int(input("Năm:"))
date = dd,mm ,yy
if 1<=mm<=12:
    if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
        if 1<=dd<=31:
            print(date)
        else:
            print('nhập lại')
    if mm == 4 or mm == 6 or mm == 9 or mm == 11:
        if 1<=dd<=30:
            print(date)
        else:
            print('nhập lại')
    if mm == 2:
        if 1<=dd<=29:
            print(date)
        else:
            print('nhập lại')
#Phần 4
#Bài 1
Username1 = input('Tên đăng nhập:')
Pass1 = input('Mật khẩu:')
Email1 = input('Email:')
l1 = '== Registration=='
l2 = 'Registered successfully'
print(l1)
print(Username1)
print(Pass1)
print(Email1)
print(l2)
#Bài 3
Username1 = input('Tên đăng nhập:')
Pass1 = input('Mật khẩu:')
Passrepeat = input('Nhập lại mật khẩu:')
Email1 = input('Email:')
l1 = '== Registration=='
l2 = 'Registered successfully'
if Pass1 == Passrepeat:
    print(l1)
    print(Username1)
    print(Pass1)
    print(Email1)
    print(l2)
while Pass1 != Passrepeat:
     Passrepeat = input('Nhập lại mật khẩu:')
     if Pass1 == Passrepeat:
        print('Registered successfully')
#Phần 5
diem = 0
import random
n1 = random.randint(1,100)
n2 = random.randint(1,100)
n3 = random.randint(1,100)
print('== FREAKING MATH CONSOLE ==')
print(n1,'/',n2,'=', n3)
tf = int(input('Nhập 1 cho đúng hoặc 2 cho sai'))
if n1/n2 == n3 and tf == 1:
    print("Đúng")
    diem += 1
    print(diem)
if n1/n2 == n3 and tf == 2:
    print('Sai')
if n1/n2 != n3 and tf == 2:
    print('Đúng')
    diem += 1
    print(diem)
if n1/n2 != n3 and tf == 1:
    print('Sai')
print(n1,'*',n2,'=', n3)
tf = int(input('Nhập 1 cho đúng hoặc 2 cho sai'))
if n1*n2 == n3 and tf == 1:
    print("Đúng")
    diem += 1
    print(diem)
if n1*n2 == n3 and tf == 2:
    print('Sai')
if n1*n2 != n3 and tf == 2:
    print('Đúng')
    diem += 1
    print(diem)
if n1*n2 != n3 and tf == 1:
    print('Sai')
print(n1,'-',n2,'=', n3)
tf = int(input('Nhập 1 cho đúng hoặc 2 cho sai'))
if n1-n2 == n3 and tf == 1:
    print("Đúng")
    diem += 1
    print(diem)
if n1-n2 == n3 and tf == 2:
    print('Sai')
if n1-n2 != n3 and tf == 2:
    print('Đúng')
    diem += 1
    print(diem)
if n1-n2 != n3 and tf == 1:
    print('Sai')
print(n1,'+',n2,'=', n3)
tf = int(input('Nhập 1 cho đúng hoặc 2 cho sai'))
if n1+n2 == n3 and tf == 1:
    print("Đúng")
    diem += 1
    print(diem)
if n1+n2 == n3 and tf == 2:
    print('Sai')
if n1+n2 != n3 and tf == 2:
    print('Đúng')
    diem += 1
    print(diem)
if n1+n2 != n3 and tf == 1:
    print('Sai')
print('== GAME OVER ==')
print('Điểm của bạn',diem)

