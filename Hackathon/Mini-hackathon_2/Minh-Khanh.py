#Phần 1
#Bài 1
arr = ['yellow','orange','blue']
#Bài 2
arr = ['yellow','orange','blue']
for i in arr:
    print(f'Danh sách màu {i}', end=' ')
#Bài 3
n = input('Màu muốn thêm:')
arr = ['yellow','orange','blue']
arr.append(n)
for i in arr:
    print(i, end = ' ')
#Phần 2
#Bài 1
n = int(input())
arr = ['yellow','orange','blue']
print(f'{arr[n-1]} là màu ở vị trí {n}')
#Bài 2
arr = ['yellow','orange','blue']
n = input()
if n.isdecimal() == True:
    arr.pop(int(n)-1)
    print(arr)
else:
    arr.remove(n)
    print(arr)
#Bài 3
import turtle
turtle.fillcolor("#ffd700")
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.fillcolor("#ffd700")
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.fillcolor("#ffd700")
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.mainloop()
#Phần 3
#Bài 1
arr = [5, 1, 8, 92, -1]
n = int(input())
for i in arr:
    if n == i:
        print(arr.index(i)+1)
#Bài 2
n = 0
arr = [5, 1, 8, 92, -1]
for i in arr:
    n = n+i
print(n)
#Bài 3
a = 0
while True:
    n = int(input())
    a = a+n
    if n==0:
        break
print(a)
#Phần 4
#Bài 1
arr = [5, 1, 8, 92, 7]
for i in arr:
    if i%2==0:
        print(i,end=' ')
#Bài 2
arr = []
while True:
    n = int(input())
    if n%2==0 and n!=0:
        arr.append(n)
    if n==0:
        break
for i in arr:
    print(i,end=' ')
#Phần 5
#Bài 1
quan = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
dan = [247100, 333300, 266800, 420900, 318000]
#Bài 2
quan = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
dan = [247100, 333300, 266800, 420900, 318000]
print(f'Quận đông nhất:{dan.index(max(dan))}')
print(f'Quận ít nhất:{dan.index(min(dan))}')
#Bài 3
quan = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
dan = [247100, 333300, 266800, 420900, 318000]
print(f'Quận đông nhất:{quan[dan.index(max(dan))]}')
print(f'Quận ít nhất:{quan[dan.index(min(dan))]}')
#Phần 6
#Bài 1
dientich = [9.224, 43.35, 12.04, 9.96, 10.09]
matdo = [26788.811795316564, 7688.581314878892, 22159.468438538206, 42259.03614457831, 31516.352824578793]
for i in matdo:
    print(i)
#Bài 2
a = 0
matdo = [26788.811795316564, 7688.581314878892, 22159.468438538206, 42259.03614457831, 31516.352824578793]
for i in matdo:
    a = a+i
print(a/5)
#Phần 7
#Bài 1
arr = [78, 56, 67]
#Bài 2
a = 0
arr = [78, 56, 67]
for i in arr:
    a = a+1
    print(a,i)
#Bài 3
a = 0
arr = []
while True:
    n = int(input())
    arr.append(n)
    if n == 0:
        break
for i in arr:
    a = a+1
    print(a,i)
#Phần 8
#Bài 1
a = 0
arr = []
while True:
    n = int(input())
    arr.append(n)
    if n == 0:
        break
arr.sort()
arr.reverse()
for i in arr:
    a = a+1
    print(a,i)
#Bài 2
a = 0
arr = []
while True:
    n = int(input())
    arr.append(n)
    if n == 0:
        break
arr.sort()
arr.reverse()
for i in arr:
    a = a+1
    if a > 5:
        break
    print(a,i)
    


