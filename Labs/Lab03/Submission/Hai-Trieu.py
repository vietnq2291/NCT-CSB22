#Bài 1:
print("Đây là bài số 1:")
number = int(input("Nhập một số nguyên bất kì: "))
if number % 2 == 0:
    print(number, "là số chẵn!")
else:
    print(number, "là số lẻ!")

#Bài 2: 
print("Đây là bài số 2:")
import math
number = float(input("Nhập một số thực bất kì: "))
if number == math.ceil(number) == math.floor(number):
    print(number, "là số nguyên!")
else:
    print(number, "không phải là số nguyên!")

#Bài 3:
print("Đây là bài số 3:")
kitu = input("Nhập một kí tự: ")
if kitu.isdigit():
    print(kitu, "là một số")
elif kitu.isalpha():
    print(kitu, "là một chữ")
else:
    print(kitu, "không phải là số và cũng không phải là chữ")


#Bài 4:
print("Đây là bài số 4:")
Numb = float(input("Nhập 1 số bất kì: "))
if Numb % 3 == 0 and Numb % 5 == 0:
    print(f"{Numb} is divisible by 3 and 5.") 
elif Numb % 3 == 0 and Numb % 5 != 0:
    print(Numb, "is divisible by 3") 
elif Numb % 5 == 0 and Numb % 3 != 0:
    print(f"{Numb} is divisible by 5.") 
else:
    print(Numb, "is not divisible by 3 and 5.")


#Bài 5:
print("Welcome to The Ultimate Security System")
print("Our company just created for you an account.")
print("Your username is: NgoQuangVietCSB22")
print("Your password is: 54321")
UserN = "NgoQuangVietCSB22"
PassW = "54321"
print("Please input again your username and password to make sure that you're not robot :)!")
UName = input("Username: ")
PWord = input("Password: ")
if UName == UserN and PWord == PassW:
    print("You're logged in,", UName, "!")
elif UName != UserN or PWord != PassW:
    print("Wrong username or password!")


#Bài 6:
a = float(input("Nhập độ dài cạnh thứ nhất: "))
b = float(input("Nhập độ dài cạnh thứ hai: "))
c = float(input("Nhập độ dài cạnh thứ ba: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Các độ dài đã cho có thể tạo thành một tam giác")
else:
    print("Các độ dài đã cho không thể tạo thành một tam giác")


#Bài 7:
a = float(input("Nhập độ dài cạnh thứ nhất: "))
b = float(input("Nhập độ dài cạnh thứ hai: "))
c = float(input("Nhập độ dài cạnh thứ ba: "))

if (a + b > c) and (a + c > b) and (b + c > a):

    if a == b == c:
        print("Tam giác đều")

        import turtle
        t = turtle.Turtle()
        t.speed(1)
        for i in range(3):
            t.forward(a)
            t.right(120)
        turtle.done()
    elif (a == b) or (b == c) or (a == c):
        if ((a * a + b * b == c * c) or (b * b + c * c == a * a) or (a * a + c * c == b * b)):
            print("Tam giác vuông cân")
        else:
            print("Tam giác cân")
    elif ((a * a + b * b == c * c) or (b * b + c * c == a * a) or (a * a + c * c == b * b)):
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Ba cạnh đã cho không thể tạo thành tam giác")