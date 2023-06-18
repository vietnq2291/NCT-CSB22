n = int(input("Input a number: "))
def gt(n):
    gt = 1
    for i in range (1,n+1):
        gt *= i
    return gt
print(f"{n}! = {gt(n)} ")
