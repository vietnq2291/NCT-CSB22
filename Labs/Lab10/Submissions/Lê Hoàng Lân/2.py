numbers2 = {
    'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14,
    'XV': 15, 'XVI': 16, 'XVII': 17, 'XVIII': 18,
    'XIX': 19, 'XX': 20
}
numbers = {
    'I':1, 'II': 2, 'III': 3, 'IV': 4,
    'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8,
    'IX': 9, 'X': 10
}
for keys in numbers2.keys():
    numbers[keys] = numbers2[keys]

uInput2 = input("Input a Roman number: ")
if uInput2 in numbers.keys():
    print(f"Arabic number: {numbers[uInput2]}")
else:
    print("Not found.")
