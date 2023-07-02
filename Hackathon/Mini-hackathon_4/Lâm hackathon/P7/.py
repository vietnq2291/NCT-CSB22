skills = [
    {
        'Name': 'Tackle',
        'Minimum level': 1,
        'Damage': 5,
        'Hit rate': 0.3
    },
    {
        'Name': 'Quick Attack',
        'Minimum level': 2,
        'Damage': 3,
        'Hit rate': 0.5
    },
    {
        'Name': 'Strong Kick',
        'Minimum level': 4,
        'Damage': 9,
        'Hit rate': 0.2
    }
]
for i in range(len(skills)):
    skill_number = i + 1
    skill_name = skills[i]['Name']
    print(f"Skill {skill_number}: {skill_name}")