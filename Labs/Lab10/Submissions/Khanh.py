#Bài 1
numbers = {
    'I': 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5,
    'VI': 6,
    'VII': 7,
    'VIII': 8,
    'IX': 9,
    'X': 10,
}
n = input('input number:')
if n in numbers:
    print(numbers[n])
else:
    print('not found')
#Bài 2
numbers = {
    'I': 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5,
    'VI': 6,
    'VII': 7,
    'VIII': 8,
    'IX': 9,
    'X': 10,
}
numbers_2 = {
    'XI': 11,
    'XII': 12,
    'XIII': 13,
    'XIV': 14,
    'XV': 15,
    'XVI': 16,
    'XVII': 17,
    'XVIII': 18,
    'XIX': 19,
    'XX': 20,
}
numbers.update(numbers_2)
n = input('input number:')
if n in numbers:
    print(numbers[n])
else:
    print('not found')
#Bài 3
numbers_list = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']
numbers = {}
for i in range(0,len(numbers_list)):
    numbers[numbers_list[i]] = i+1
n = input('input number:')
if n in numbers:
    print(numbers[n])
else:
    print('not found')
#Bài 6
n = input('nhập:')
dict = {}
arr = []
for t in n:
    arr.append(t)
for item in arr:
    a = arr.count(item)
    dict[item] = a
print(f"tần số", dict)
