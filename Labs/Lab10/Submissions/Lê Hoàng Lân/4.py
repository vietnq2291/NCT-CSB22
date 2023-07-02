students = [{'firstName': 'Nikki', 'lastName': 'Roysden'}, 
            {'firstName': 'Mervin', 'lastName': 'Friedland'}, 
            {'firstName': 'Aron', 'lastName': 'Wilkins'}]

print("List of students:")
for item in range(len(students)):
    print(f"- {students[item]['firstName']} {students[item]['lastName']}")
print()