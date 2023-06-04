sc = [1,2,3,4,5,6,7,8,9,10]
sc.sort()
print("High scores: ")
for x in range(1,4):
    print(f"{x}. {sc[-x]}")