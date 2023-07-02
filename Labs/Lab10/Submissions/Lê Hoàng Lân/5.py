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
