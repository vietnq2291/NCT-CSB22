# Bài 1
r = float(input("Nhập độ dài bán kính:"))
pi = 3.1416
P = 2*pi*r
S = pi*r*r
print("Chu vi hình tròn:",P)
print("Diện tích hình tròn:",S)

# Bài 2
import math
a = float(input("Nhập độ dài cạnh hình vuông:"))
DuongCheo = a*math.sqrt(2)
print("Đường chéo hình vuông:",DuongCheo)

# Bài 3
username = input("Account name:")
domain = input("Domain name:")
print(f"Full email: {username}{domain}")

# Bài 4
Date = input(f"Date in MM/DD/YYYY: ")
abc = Date.split("/")
print(f"Date in DD/MM/YYYY: {abc[1]}/{abc[0]}/{abc[2]}")

# Bài 5
Deposit = float(input("Deposit: "))
print("Account after 1 year:",Deposit*1.05**1)
print("Account after 2 years:",Deposit*1.05**2)
print("Account after 10 years:",Deposit*1.05**10)

# Bài 6
import turtle as t
t.fd(100)
t.rt(90)
t.pensize(5)
t.pencolor('#de5246')
t.fd(70)
t.rt(90)
t.pencolor('black')
t.pensize(1)
t.fd(100)
t.rt(90)
t.pensize(5)
t.pencolor('#de5246')
t.fd(70)
t.rt(90+35)
t.fd(60)
t.lt(70)
t.fd(60)
t.pu()
t.rt(180)
t.fd(60)
t.rt(125)
t.fd(70)

# Bài 7
import turtle as t
t.resetscreen()
t.pencolor('#cf8f03')
t.pensize(10)
t.rt(22)
t.fd(100)
t.rt(135)
t.fd(100)
t.rt(45)
t.fd(100)
t.rt(135)
t.fd(100)
t.rt(22)
t.pu()
t.fd(50)
t.pd()
t.pencolor('#0b2c3c')
t.rt(22)
t.fd(100)
t.rt(135)
t.fd(100)
t.rt(45)
t.fd(100)
t.rt(135)
t.fd(100)