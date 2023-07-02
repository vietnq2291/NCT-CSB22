# Bài 1
numbers = {
    'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
    'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10
}
user_input = input("Input a Roman number: ")
if user_input in numbers.keys():
    print(f"Arabic number: {numbers[user_input]}")
else:
    print("Not found.")

# Bài 2
numbers_2 = {
    'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15,
    'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20
}
numbers.update(numbers_2)
user_input = input("Input a Roman number: ")
if user_input in numbers.keys():
    print(f"Arabic number: {numbers[user_input]}")
else:
    print("Not found.")

# Bài 3
number_list = [
    'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
    'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX'
]
number_dict = {}

for i in range(len(number_list)):
    number_dict[number_list[i]] = i + 1

user_input = input("Input a Roman number: ")
if user_input in number_dict.keys():
    print(f"Arabic number: {number_dict[user_input]}")
else:
    print("Not found.")

# Bài 4
students = [
    {'firstName': 'Nikki', 'lastName': 'Roysden'},
    {'firstName': 'Mervin', 'lastName': 'Friedland'},
    {'firstName': 'Aron', 'lastName': 'Wilkins'}
]
print("List of students:")
for stu in students:
    print("-", stu['firstName'], stu['lastName'])

# Bài 5
names = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}
print("List of students:")
for student in names['students']:
    print("-", student['firstName'], student['lastName'])

print("List of teachers:")
for teacher in names['teachers']:
    print("-", teacher['firstName'], teacher['lastName'])

# Bài 6
input_sequence = input("Input sequence: ")

freq = {}
for char in input_sequence:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Frequency of characters:")
print(freq)