city_data = [
    ["BĐ", 9.224, 247100],
    ["BTL", 43.35, 333300],
    ["CG", 12.04, 266800],
    ["ĐĐ", 9.96, 420900],
    ["HBT", 10.09, 318000]
]
names = [row[0] for row in city_data]
populations = [row[2] for row in city_data]
print("tên cách quận là:",names)
print("Dân số các quận:",populations)