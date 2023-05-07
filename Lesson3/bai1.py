a = float(input("Number 1: "))
b = float(input("Number 2: "))
c = float(input("Number 3: "))

if a > b  and a > c:
    print(f"The largest number is {a}")
elif b > a  and b > c:
    print(f"The largest number is {b}")
elif c > b  and c > a:
    print(f"The largest number is {c}")