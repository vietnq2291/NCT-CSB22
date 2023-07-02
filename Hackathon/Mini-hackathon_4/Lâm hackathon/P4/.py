# Bài 1
cost = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400,
}
print(f"Total price: {cost['ASUS'] * 5}")

# Bài 2
cost = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400,
}
brand = input("Input a brand: ")
amount = int(input("Input amount to buy: "))
print(f"Total price: {cost[brand] * amount}")

# Bài 3
com_cost = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400,
}
com_amount = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}
brand = input("Input a brand: ")
amount = int(input("Input amount to buy: "))

if brand in com_amount:
    print(f"Total price: {com_cost[brand] * amount}")
    com_amount[brand] -= amount
    print("Available products:")
    for br, it in com_amount.items():
        print(f"- {br}: {it}")
else:
    print("Brand not found")