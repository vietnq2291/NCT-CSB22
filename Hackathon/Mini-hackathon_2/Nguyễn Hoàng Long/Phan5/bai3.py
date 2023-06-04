city_data = [
    ["BĐ", 9.224, 247100],
    ["BTL", 43.35, 333300],
    ["CG", 12.04, 266800],
    ["ĐĐ", 9.96, 420900],
    ["HBT", 10.09, 318000]
]
populations = [247100, 333300, 266800, 420900, 318000]
max_index = populations.index(max(populations))
min_index = populations.index(min(populations))

namesMax = city_data[max_index]
namesMin = city_data[min_index]
print(f"quận có dân số cao nhất",namesMax)
print(f"quận có dân số thấp nhất",namesMin)