def fac(x):
    if x < 0:
        return None
    elif x == 0 or x == 1:
        return 1
    else:
        a = 1
        for i in range(2, x+1):
            a = a * i
        return a

num = int(input("Input a number: "))
res = fac(num)
if res is None:
    print("Can't solve")
else:
    print(f"{num}! = {res}")