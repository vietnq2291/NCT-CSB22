import math

#BT1:
numA = int(input("Number 1: "))
numB = int(input("Number 2: "))
numC = int(input("Number 3: "))
if numA > numB and numA > numC:
    print(f"The largest number is: {numA}")
elif numB > numA and numB > numC:
    print(f"The largest number is: {numB}")
else:
    print(f"The largest number is: {numC}")

#BT2: 
yearInput = int(input("Year: "))
if yearInput %  4 == 0:
    print(f"{yearInput} is a leap year.")
elif yearInput % 400 == 0:
    print(f"{yearInput} is a leap year.")
else:
    print(f"{yearInput} is not a leap year.")

#BT3: 
print("Quadratic equation")
numA2 = float(input("a: "))
numB2 = float(input("b: "))
numC2 = float(input("b: "))
delta = (numB2**2 - (4*numA2*numC2))
if delta > 0:
    res1 = ((-numB2 + math.sqrt(delta))/2*numA2)
    res2 = ((-numB2 - math.sqrt(delta))/2*numA2)
    print(f"x1 = {res1}\nx2 = {res2}")
elif delta == 0:
    root = -(numB2/2*numA2)
    print(f"Root: {root}")
else:
    print("No solutions!")