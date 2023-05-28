#Bài 1
n = int(input())
for i in range(n):
    print('#'*(i+1))
#Bài 2
N = int(input())
if N > 0:
    print('số dương')
else:
    print('nhập lại')
#Bài 3
N = int(input())
if N>0:
    a = 1
    for i in range(N):
        a = a*i
    print(a)
if N==0:
    print('0')
if N!=0:
    print('Invalid')
#Bài 4
N = int(input())
a = 0
for i in range(len(str(N))):
    a = a + int(str(N)[i])
print(a)
#Bài 6
import turtle
N = int(input())
canh = 100
goc = (N-2)*180
for i in range(N):
    turtle.forward(100)
    turtle.right(180-(goc/N))
    turtle.mainloop
