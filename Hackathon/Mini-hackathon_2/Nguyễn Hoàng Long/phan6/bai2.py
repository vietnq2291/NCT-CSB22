city_data = [
    ["BĐ", 9.224, 247100],
    ["BTL", 43.35, 333300],
    ["CG", 12.04, 266800],
    ["ĐĐ", 9.96, 420900],
    ["HBT", 10.09, 318000]
]
populations = [247100, 333300, 266800, 420900, 318000]
areas = [data[1] for data in city_data]
densities = [pop / area for pop, area in zip(populations, areas)]
avg_density = sum(densities) / len(densities)

print("Mật độ dân số trung bình của các quận:", avg_density)
