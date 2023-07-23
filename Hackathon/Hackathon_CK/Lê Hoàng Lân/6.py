a = int(input("Input a number: "))
c=0
while a >= 1:
    b = a % 10
    c+=1
    a=a/10
print(f'This number has {c} digit(s)')