character = {
"Name": "Light",
"Age": 17,
"Strength": 8,
"Defense": 10,
"HP": 100,
"Backpack": ["Shield", "Bread Loaf"],
"Gold": 100,
"Level": 2
}
character["Gold"] += 50
print("số gold mới của charater:",character["Gold"])

character["Backpack"].append("FlintStone")
print("Backpack mới của nhân vật là:", character["Backpack"])