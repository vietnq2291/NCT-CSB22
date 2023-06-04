# B1
arr = [5, 1, 8, 92, -1, 30]
print(arr)
inp = int(input("Input number: "))
if inp in arr:
    pos = arr.index(inp) + 1
    print(f"Number found at position {pos}")
else:
    print("Number not found")

# B2
arr1 = [5, 1, 8, 92, -1]
print(arr1)
print(f"Sum of all numbers: {sum(arr1)}")

# B3
num = []
print("Input the list of numbers.\nEnter 0 to finish.")
while True:
    inp = int(input())
    if inp == 0:
        break
    num.append(inp)
print(f"Sum of numbers in list: {sum(num)}")