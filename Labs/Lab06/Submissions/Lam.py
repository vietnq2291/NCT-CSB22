# Bài 1
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = []
arr3 = []

for i in arr1:
    arr2.append(i+2)
print(f"Add 2\t     : {arr2}")
for i in arr1:
    arr3.append(i*2)
print(f"Multiply by 2: {arr3}")

# Bài 2
arr = ["l", "o", "o", "h", "c", "s", " ", "y", "g", "o", "l", "o", "n", "h", "c", "e", "T", " ", "X", "d", "n", "i", "M"]
arr.reverse()
print(arr)

# Bài 3
inp = int(input("Input a positive number: "))
arr = [1, 1]
next_ele = 0
for i in range(inp - 2):
    next_ele = arr[i] + arr[i + 1]
    arr.append(next_ele)
print(f"First {inp} Fibonacci number(s): {arr}")

# Bài 4

