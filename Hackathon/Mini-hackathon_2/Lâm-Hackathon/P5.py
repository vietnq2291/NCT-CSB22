# B1
districts = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
populations = [247100, 333300, 266800, 420900, 318000]

# B2
print("Indices of:")
max_population_index = populations.index(max(populations))
min_population_index = populations.index(min(populations))
print(f"Most populated dist: {populations.index(max(populations))}")
print(f"Least populated dist: {populations.index(min(populations))}")

# B3
print("Names of:")
max_population_district = districts[max_population_index]
min_population_district = districts[min_population_index]
print(f"Most populated dist: {districts[max_population_index]}")
print(f"Least populated dist: {districts[min_population_index]}")