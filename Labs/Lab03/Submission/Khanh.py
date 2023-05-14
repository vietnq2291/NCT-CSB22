#Bài 1
n = int(input())
if n%2 == 0:
    print('số chẵn')
else:
    print('số lẻ')
#Bài 2
N = float(input())
if N == N//1:
    print('Số nguyên')
else:
    print('Không phải số nguyên')
#Bài 3
a = input()
if a.isdecimal() == True:
    print('đây là số')
else:
    print('đây k là số')
#Bài 4
A = int(input())
if A%3==0 and A%5==0:
    print('A chia hết cho 3 và 5')
if A%3==0 and A%5!=0:
    print('A chia hết cho 3 và k chia hết cho 5')
if A%3!=0 and A%5==0:
    print('A k chia hết cho 3 và chia hết cho 5')
if A%3!=0 and A%5!=0:
    print('A k chia hết cho 3 và 5')
#Bài 5
Username = input('Username:')
Pass = input('Password:')
if Username == 'admin' and Pass == '12345':
    print('Đăng nhập thành công')
else:
    print('Nhập sai tên đăng nhập hoặc mật khẩu')
#Bài 6
c1 = float(input('cạnh 1:'))
c2 = float(input('cạnh 2:'))
c3 = float(input('cạnh 3:'))
if c1>0 and c2>0 and c3>0:
    if c1+c2>c3 and c1+c3>c2 and c2+c3>c1:
        print('đây là tam giác')
    else:
        print('Đây không là tam giác')
else:
    print('nhập lại')
#Bài 7
C1 = float(input('cạnh 1:'))
C2 = float(input('cạnh 2:'))
C3 = float(input('cạnh 3:'))
if C1>0 and C2>0 and C3>0:
    if C1**2+C2**2==C3**2 or C1**2+C3**2==C2**2 or C2**2+C3**2==C1**2:
        print('đây là tam giác vuông')
    if C1==C2==C3:
        print('đây là tam tác đều')
        import turtle
        turtle.forward(C1)
        turtle.right(120)
        turtle.forward(C1)
        turtle.right(120)
        turtle.forward(C1)
        turtle.mainloop()
    if C1+C2>C3 and C1+C3>C2 and C2+C3>C1:
        print('đây là tam giác thường')   
    else:
        print('đây k là tam giác')
else:
    print('nhập lại')

