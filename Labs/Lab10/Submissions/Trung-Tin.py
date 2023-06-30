#BT1: 
numbers = {
    'I':1, 'II': 2, 'III': 3, 'IV': 4,
    'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8,
    'IX': 9, 'X': 10
}

uInput1 = input("Input a Roman number: ")
if uInput1 in numbers.keys():
    print(f"Arabic number: {numbers[uInput1]}")
else:
    print("Not found.")

#BT2: 
numbers2 = {
    'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14,
    'XV': 15, 'XVI': 16, 'XVII': 17, 'XVIII': 18,
    'XIX': 19, 'XX': 20
}

for keys in numbers2.keys():
    numbers[keys] = numbers2[keys]

uInput2 = input("Input a Roman number: ")
if uInput2 in numbers.keys():
    print(f"Arabic number: {numbers[uInput2]}")
else:
    print("Not found.")

#BT3: 
number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 
               'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

newDict = {}
for keys in range(0, len(number_list)):
    newDict[number_list[keys]] = keys+1

uInput3 = input("Input a Roman number: ")
if uInput3 in numbers.keys():
    print(f"Arabic number: {numbers[uInput3]}")
else:
    print("Not found.")

#BT4:
students = [{'firstName': 'Nikki', 'lastName': 'Roysden'}, 
            {'firstName': 'Mervin', 'lastName': 'Friedland'}, 
            {'firstName': 'Aron', 'lastName': 'Wilkins'}]

print("List of students:")
for item in range(len(students)):
    print(f"- {students[item]['firstName']} {students[item]['lastName']}")
print()
#BT5: 
names = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'}, 
        {'firstName': 'Mervin', 'lastName': 'Friedland'}, 
        {'firstName': 'Aron', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'}, 
        {'firstName': 'Regine', 'lastName': 'Agtarap'}, 
    ],
}

for group in names.keys():
    print(f"List of {group}.")
    for person in names[group]:
        print(f"- {person['firstName']} {person['lastName']}")

#BT6: 
uInput3 = input("Input sequence: ")
newDict2 = {}
process = []
for letterorword in uInput3:
    process.append(letterorword)
for item in process:
    instances = process.count(item)
    newDict2[item] = instances
print(newDict2)
