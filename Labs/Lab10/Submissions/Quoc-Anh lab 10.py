# # BT1
# dict1 = {
#     'I': 1,
#     'II': 2,
#     'III': 3,
#     'IV': 4,
#     'V': 5,
#     'VI': 6,
#     'VII': 7,
#     'VIII': 8,
#     'IV': 9,
#     'X': 10
# }
# Roman_num = (input("Input a Roman number: "))
# if Roman_num in dict1:
#     print ("Arabic number:",dict1[Roman_num])
# else: 
#     print ("Not Found.")
    
# # BT2
# dict2 = {
#     'XI': 11,
#     'XII': 12,
#     'XIII': 13,
#     'XIV': 14,
#     'XV': 15,
#     'XVI': 16,
#     'XVII': 17,
#     'XVIII': 18,
#     'XI': 19,
#     'XX': 20
#     }
# dict1.update(dict2)
# Roman_num = (input("Input a Roman number: "))
# if Roman_num in dict2:
#     print ("Arabic number:",dict2[Roman_num])
# else: 
#     print ("Not Found.")

# # BT3
# roman_number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
# arab_number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# dict3 = {}
# for i in range(len(roman_number_list)):
#     dict3[roman_number_list[i]] = arab_number_list[i]
# Roman_num = (input("Input a Roman number: "))
# if Roman_num in dict3:
#     print ("Arabic number:",dict3[Roman_num])
# else: 
#     print ("Not Found.")
    
# BT4
students = [{'firstName': 'Nikki','lastName': 'Roysden'},
            {'firstName': 'Mervin','lastName': 'Friedland'},
            {'firstName': 'Aron','lastName': 'Wilkins'}]

print ("List of students:")
for i in range(len(students)):
    print ("-",students[i]['firstName'], students[i]['lastName'])
    
# BT5
names = {'students':[
        {'firstName': 'Nikki','lastName': 'Roysden'},
        {'firstName': 'Mervin','lastName': 'Friedland'},
        {'firstName': 'Aron','lastName': 'Wilkins'}],
'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'},
            {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

for group in names.keys():
    print (f'List of {group}:')
    for people in names[group]:
        print ('-',people['firstName'], people['lastName'])

# BT6
sequence = input("Input sequence: ")
dict6 = {} 
letter_database = []
for letters in sequence:
    letter_database.append(letters)
for i in letter_database:
    x = letter_database.count(i)
    dict6 [i] = x
print (f'Frequency of characters: {dict6}')
 
     
    
    
    

 
    