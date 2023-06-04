sc = [1,2,3,4,5,6,7,8,9,10]
ad = int(input("Input new score: "))
sc.append(ad)
sc.sort()
for x in range(1,6):
    print(f"{x}. {sc[-x]}")