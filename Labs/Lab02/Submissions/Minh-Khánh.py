pi = 3.14165
r = float(input())
P = 2*pi*r
S = pi*r**2
print(P)
print(S)


import math
canh = float(input())
duongcheo = math.sqrt(canh**2+canh**2)
print(duongcheo)


ten = input()
duoi = "@gmail.com"
email = ten + duoi
print(email)


DD = input('ngày:')
MM = input('tháng:')
YY = input('năm:')
Ngay = DD+ '/' + MM + '/' + YY
print(Ngay)


Tien = int(input('Số tiền gửi:'))
Nam = int(input('Số năm gửi:'))
Tongtienlai = Tien*(105/100)**Nam
print(Tongtienlai)


import turtle
turtle.forward(150)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.right(65)
turtle.forward(85)
turtle.right(50)
turtle.forward(85)
turtle.mainloop()
