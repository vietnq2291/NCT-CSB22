 
def bt (x):
    gt = 1
    for i in range (1,x):
        gt *= i
    pt = 0
    for y in range (1,x):
        pt += gt(x)/y
    return pt 


x = int(input("Input a number: "))
print ("Result:",bt(x))