arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = []
arr3 = []
c=0
for x in arr1:
    arr2.append(x+2)

for y in arr1:
    arr3.append(y*2)

print(f"{arr2}\n{arr3}")