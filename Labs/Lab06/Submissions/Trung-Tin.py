#BT1: 
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = []
arr3 = []

for x in arr1:
    arr2.append(x+2)
for y in arr1:
    arr3.append(y*2)

print(f"{arr2}\n{arr3}")

#BT2:
arrDigits = ["l", "o", "o", "h", "c", "s", " ", "y", "g", "o", "l", "o", "n", "h", "c", "e", "T", " ", "X", "d", "n", "i", "M"]
arrDigits.reverse()
print(arrDigits)

#BT3: 
pInput = int(input("Input positive number: "))
result = ""
baseN1 = 0
baseN2 = 1
for x in range(1, pInput):
    nextN = baseN1 + baseN2
    baseN1 = baseN2
    baseN2 = nextN
    result += f"{nextN} "
print(f"First {pInput} fibonacci number(s): {result}")

#BT4: 
arrFoods = [("Ribeye Steak", 30.5), ("Potato Salad", 5), ("Sparkling Wine", 7), ("Smoked Salmon", 12), ("Chicken Soup", 8.5), ("Tiramisu Cake", 4.5)]
tPrice = 0
print(f"\nNumber of items: {len(arrFoods)}")
for x in range(len(arrFoods)):
    print(f"\nItem {x+1}: {arrFoods[x][0]}")
    print(f"Price of item {x+1}: {arrFoods[x][1]}")
    tPrice += arrFoods[x][1]
fPrice = tPrice/len(arrFoods)
print(f"\nAverage price: {fPrice}")
aboveAvg = ""
for x in range(len(arrFoods)):
    if arrFoods[x][1] > fPrice:
        aboveAvg += f"{arrFoods[x]} "
print(f"Item(s) above average price: {aboveAvg}")

#BT5: 
wordCount = 0
exword_list = []
while True: 
    sInput = input("Write a sentence: ")
    sInput.lower()
    word_list = sInput.split(" ")
    if sInput == "quit":
        break
    else: 
        for x in word_list:
            if x not in exword_list:
                wordCount += 1
                exword_list.append(x)
        print(f"Number of unique words: {wordCount}")