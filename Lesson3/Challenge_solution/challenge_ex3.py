import math

# eq: ax^2 + bx + c = 0
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("A quadratic equation must satisfy condition a != 0")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("The equation has no solution!")
    elif delta == 0:
        root = - b / (2*a)
        print("root =", root)
    else:
        root1 = (-b - math.sqrt(delta)) / (2*a)
        root2 = (-b + math.sqrt(delta)) / (2*a)
        print("Solution:")
        print(" x1 =", root1)
        print(" x2 =", root2)