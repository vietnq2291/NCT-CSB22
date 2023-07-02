computer_inventory = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

computer_inventory["DELL"] = 60
computer_inventory["MACBOOK"] = 2

print("Available products:")
for brand, quantity in computer_inventory.items():
    print(f"- {brand}: {quantity}")
