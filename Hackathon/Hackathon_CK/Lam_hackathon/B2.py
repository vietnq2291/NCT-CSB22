import math

def equation(a,b,c):
    delta = b**2 - 4*a*c

    if delta < 0:
        print("The equation has no solution")
    elif delta == 0:
        x = -b / (2*a)
        print("The quation has 1 double root")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("The equation has 2 solutions.")
        print(f"x = {x1} or x = {x2}")

a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

equation(a,b,c)
