#skill Nhan vat
skills = [
{
"Name": "Tackle",
"Minimum level": 1,
"Damage": 5,
"Hit rate": 0.3
},
{
"Name": "Quick Attack",
"Minimum level": 2,
"Damage": 3,
"Hit rate": 0.5
},
{
"Name": "Strong Kick",
"Minimum level": 4,
"Damage": 9,
"Hit rate": 0.2
},
]

for i, skill in enumerate(skills, start=1):
    print("skill ",i, skill["Name"])
select_skill=input("Chọn skill(nhap so skill):")
select_skill_index = int(select_skill)-1

if select_skill_index < 0 or select_skill_index >= len(skills):
    print("Skill không tồn tại!")
else:
    select_skill = skills[select_skill_index]
    required_level = select_skill["Minimum level"]
    damage = select_skill["Damage"]

# Kiểm tra level
    player_level = 4  # Thay đổi level của nhân vật ở đây
    if player_level < required_level:
        print("Cannot deploy. Required level", required_level)
    else:
        print("You chose", select_skill["Name"])
        print("Damage:", damage)