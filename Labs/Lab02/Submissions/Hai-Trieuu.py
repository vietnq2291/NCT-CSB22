#Bài 1:
print("Đây là bài số 1")
import math
banKinh = float(input("Nhap ban kinh cua hinh tron: "))
chuVi = 2 * banKinh * math.pi
dienTich = banKinh ** 2 * math.pi
print("Radius:", banKinh)
print("Perimeter:", chuVi)
print("Area:", dienTich)


#Bài 2:
print("Đây là bài số 2")
canh = float(input("Nhập độ dài cạnh của hình vuông: "))
duongCheo = canh * (2 ** 0.5)
print("Length of edge:", canh)
print("Length of diagonal line:", duongCheo)



#Bài 3:
print("Đây là bài số 3")
Account_name = input('Input your account name (ex: haitrieu): ')
Domain_name = input('Input your domain name (ex: 2006):' + " ")
Born_year = input("Input your born year (ex: gmail.com):" + " ")
#Đăt những ngoặc nhọn trog nháy kép hoặc đơn sao cho đúng theo thứ tự phần tử trong format hoặc ngược lại hoặc tùy trường hợp
Email = "{}{}@{}".format(Account_name, Born_year, Domain_name)
#Email = Account_name + Domain_name
print("Tài khoản email của bạn là: ", Email)




#Bài 4:
print("Đây là bài số 4:")
Day = input("Input today's date: ")
Month = input("Input today's month: ")
Year = input("Input today's year: ")
M_D_Y = "{}/{}/{}".format(Month, Day, Year)
D_M_Y = "{}/{}/{}".format(Day, Month, Year)
print("Day in MM/DD/YYYY format: ", M_D_Y)
print("Day in DD/MM/YYYY format: ", D_M_Y)



#Bài 5:
print("Đây là bài 5:")
Deposit =  float(input("Input the amount of your deposit (ex: 200.000): "))
Amount_year = float(input("Input the number of years you deposit your amount: "))
Total = Deposit * 1.05 * Amount_year
print("Account after", Amount_year, "years: ", Total)



#Bài 6:
print("Đây là bài số 6:")
#-------------cách import 2----------------#
import turtle as t
t.pensize(2)
t.forward(180)
t.right(90)
t.forward(100)
t.right(90)
t.forward(180)
t.right(90)
t.forward(100) 
t.left(180)
t.speed(1)
t.color('#de5246')
t.pensize(8)
t.forward(100)
t.left(180)
t.forward(100)
t.right(138)
t.forward(140)
t.left(101)
t.forward(136)
t.right(143)
t.forward(100)
t.right(90)
t.penup()
t.forward(88)
t.right(90)
t.forward(150)

t.mainloop


#Bài 7:
print("Đây là bài số 7:")
import turtle as t

#cái 1
t.penup()  
t.goto(-50, 0)  
t.pendown()
t.right(45)
t.pensize(5)
t.pencolor('#cf8f03')
t.forward(120)
t.right(90)
t.forward(120)
t.right(90)
t.forward(120)
t.right(90)
t.forward(120)
t.right(45)

#cái 2
t.penup()
t.goto(55, -5)
t.pendown()
t.right(45)
t.pencolor('#0b2c3c')
t.forward(120)
t.right(90)
t.forward(120)
t.right(90)
t.forward(120)
t.right(90)
t.forward(120)

t.done()
