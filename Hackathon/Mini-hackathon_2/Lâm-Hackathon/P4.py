# B1
arr = [5, 1, 8, 92, 7, 30]
print(arr)
arr1 = []
for i in arr:
    if i % 2 == 0:
        arr1.append(i)
print(f"Even numbers: {arr1}")

# B2
num = []
print("Input the list of numbers.\nEnter 0 to finish.")
while True:
    arr2 = []
    inp = int(input())
    arr2.append(inp)
    if inp == 0:
        break
    for i in arr2:
        if i % 2 == 0:
            num.append(i)
print(f"Even numbers in list: {num}")