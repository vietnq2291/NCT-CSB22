# Bài 1
com_amount = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}
com_cost = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400,
}
print("Total value of available brands:")
for x, y in com_cost.items():
    print(f"- {x}: {y * com_amount[x]}")

# Bài 2
com_amount = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}
com_cost = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400,
}
com = {}

print("Total value of available items:")
for x, y in com_cost.items():
    com[x] = y * com_amount[x]
print(f"Total products: {sum(com.values())}")
