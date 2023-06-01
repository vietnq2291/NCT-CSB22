#Phần 1:
print("Bài 1 (Full name):")
F_name = input("First name: ")
L_name = input("Last name: ")
Full_name = F_name + " " + L_name
print("Your full name is", Full_name, "!")

#--------------------------#
print("Bài 2 (Capitalized name):")
sth = input("Your input: ")
sth_inhoa = sth.upper()
print(sth_inhoa)




#------------------------------#
print("Bài 3 (Square number):")
Number = int(input("Input a number: "))
Sq_number = Number**2
print("Squared input: ", Sq_number)




#----------------------#
print("Bài 4 (Turtle with custom radius):")
print("Nhập số >= 50 để hình to dễ nhìn!!")
r =int(input("Input circle's radius: "))
import turtle as t
t.pensize(10)
t.circle(r)
t.done()


##
##
##


#Phần 2:
print("Bài 1")
t = 3
for i in range(10):
    print(t + i)



#----------------------------#
print("Bài 2:")
Number = int(input("Input number > 0: "))
if Number > 0:
    t = 0
    for i in range(Number+1):
      print(i)
else:
    print("Wrong!")



#-------------------------------#
print("Bài 3:")
n = int(input("Input number: "))
for i in range(1, n+1, 2):
    print(i)



#_________________________________________#
print("Bài 4:")
print("Please input the box below number > 2")
canh = int(input("Number of edges: "))
if canh > 2:
    if canh == 3: 
        Docanh = 180 - (180/canh)
        print(Docanh)
        for x in range(canh):
            import turtle as t
            t.pensize(7)
            t.forward(100)
            t.right(Docanh)
    elif canh > 3:
        Docanh = 360 - (canh-1)*(360/canh)
        print(Docanh)
        for x in range(canh):
            import turtle as t
            t.pensize(5)
            t.forward(100)
            t.right(Docanh)



######
#####
#####
###

#Phần 3:
print("Bài 1:")
number = int(input("Input number: "))
if number > 13:
    print(number, "is larger than 13")
elif number <= 13:
    print(number, "is not larger than 13")



#-------------------------------------#
print("Bài 2:")
number = int(input("Input a number: "))
if number % 2 ==0:
    print(number, "is even")
elif number % 2 != 0:
    print(number, "is not even")



#-------------------------------------#
print("Bài 3:")
Month = int(input("Nhập vào một tháng trong năm (số!!): "))
if Month in (1, 3, 5, 7, 8, 10, 12):
    Days_in_Month = 31
elif Month in (4, 6, 9, 11):
    Days_in_Month = 30
elif Month == 2:
    Year = int(input("Nhập vào một năm: "))
    if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
        Days_in_Month = 29
    else:
        Days_in_Month = 28
print("Tháng", Month, "có", Days_in_Month, "ngày.")


###
###
###


#Phần 4:
print("Bài 1:")
print("== Registration ==")
U_name = input("Username: ")
P_word = input("Password: ")
Email = input("Email (ex: abc@gmail.com): ")
print("Registered successfully.")



#----_--------------------------------#
print("Bài 2:")
print("== Registration ==")
print("Our company just created for you an account.")
print("Your username is: NgoQuangViet")
print("Your password is: 54321")
UserN = "NgoQuangViet"
PassW = "54321"
print("Please input again your username and password to make sure that you're not scammer or robot :)!")
UName = input("Repeat username: ")
PWord = input("Repeat password: ")
if UName == UserN and PWord == PassW:
    print("You're logged in,", UName, "!")
elif UName != UserN or PWord != PassW:
    print("Wrong username or password!")



#---------------------------------------------------#
print("Bài 3:")
Email = ''
Password = ''
while '@' not in Email or '.' not in Email:
    Email = input("Nhập địa chỉ email của bạn (vd: abc@gmail.com): ")


while len(Password) < 8 or not any(char.isdigit() for char in Password) or not any(char.isalpha() for char in Password):
    Password = input("Nhập mật khẩu của bạn (tối thiểu 8 ký tự và bao gồm cả chữ và số): ")

print("Email và mật khẩu hợp lệ!")
