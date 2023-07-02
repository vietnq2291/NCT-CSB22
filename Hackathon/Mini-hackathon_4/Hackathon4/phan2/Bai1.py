computer_inventory = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
computer_inventory["TOSHIBA"] = 10

print("Toshiba:")
for brand, quantity in computer_inventory.items():
    print(f"- {brand}: {quantity}")
