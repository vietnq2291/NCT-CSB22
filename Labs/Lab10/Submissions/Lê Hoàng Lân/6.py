n = input("Input sequence: ")
l1 = []
newDict = {}
for char in n:
    l1.append(char)
for item in l1:
    n = l1.count(item)
    newDict[item] = n
print(f"Frequency of characters:\n", newDict)