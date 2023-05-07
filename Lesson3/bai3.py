a = float(input("Number 1: "))
b = float(input("Number 2: "))
c = float(input("Number 3: "))
if a < 0:
    print("This equation has no solution")
delta = b**2 - 4*a*c
if delta == 0:
    print (f(root = {-b/2*a}))
x1= (-b + delta**(1/2))/(2*a)
x2= (-b - delta**(1/2))/(2*a)
print("Solution:")
print(x1)
print(x2)