# Bài 1
a = int(input("Input number: "))
for i in range(a):
    print("#"*(i+1))

# Bài 2
while True: 
    num = float(input("Input a positive number: "))
    if num > 0: 
        print("Thank you.")
        break

# Bài 3
gt = int(input("Input number: "))
if gt >= 1:
    a = 1
    for i in range(1, gt + 1):
        a = a * i
    print(f"{gt}! = {a}")
elif gt == 0:
    print(f"{gt}! = 1")
else:
    print("Invalid")
